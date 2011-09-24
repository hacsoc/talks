from collections import OrderedDict
import datetime
import glob
import os
import re
import sys

import jinja2
import yaml

GIT_RE = re.compile(r'\s+url = git://github.com/hacsoc/(?P<name>.*)\.git\n')

def submodule_name_map():
    submodules = {}

    with open('.gitmodules', 'r') as f:
        k = None
        for line in f:
            m = GIT_RE.match(line)
            if m:
                submodules[k] = m.group('name')
                k = None
            elif 'path' in line:
                k = line.split('path = ', 1)[1][:-1]

    return submodules

def parse_info_yaml(path):
    submodules = submodule_name_map()
    with open(path, 'r') as f:
        d = yaml.load(f)
        d.setdefault('audio', None)
        d.setdefault('video', None)
        d.setdefault('links', [])
        d['formats'] = OrderedDict()
        for prespath in glob.glob(os.path.join(path, "presentation.*")):
            fmt = os.path.splitext(prespath)[1][1:]
            d['formats'][fmt] = os.path.join(path, prespath)
        if path in submodules:
            d['github'] = 'http://www.github.com/hacsoc/{0}'.format(submodules[path])
        else:
            d['github'] = 'http://www.github.com/hacsoc/talks/tree/master/{0}'.format(path)
    return d

def data_for_repos():
    unsorted_data = {}
    for path in os.listdir('.'):
        if os.path.isdir(path) and path.startswith('2'):
            date_str, title = path.split(' ', 1)
            date_obj = datetime.datetime.strptime(date_str, '%Y%m%d')
            try:
                unsorted_data[path] = parse_info_yaml(os.path.join(path, 'info.yaml'))
                unsorted_data[path]['title'] = title
                unsorted_data[path]['date'] = date_obj.strftime('%B %d, %Y')
                unsorted_data[path]['date_obj'] = date_obj
            except IOError:
                print('{0} does not have an info.yaml file and will not appear on the page.'.format(path))

    key = lambda d: unsorted_data[d]['date_obj']
    return [unsorted_data[k] for k in sorted(unsorted_data.keys(),
                                             key=key, reverse=True)]

def render_talks(talks):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    t = env.get_template('template.html')
    with open('index.html', 'w') as f:
        f.write(t.render(talks=talks))

if __name__ == '__main__':
    render_talks(data_for_repos())
