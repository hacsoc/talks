#!/usr/bin/python3
from collections import OrderedDict
import datetime
import glob
import os
import re
import sys

import jinja2
import yaml

GIT_RE = re.compile(r'\s+url = git://github.com/hacsoc/(?P<name>.*)\.git\n')
PATH_RE = re.compile(r'\s+path = (?P<path>.*)\n')

def submodule_name_map():
    submodules = {}

    with open('.gitmodules', 'r') as f:
        k = None
        for line in f:
            gm = GIT_RE.match(line)
            pm = PATH_RE.match(line)
            if gm:
                submodules[k] = gm.group('name')
                k = None
            elif pm:
                k = pm.group('path')

    return submodules

SUBMODULE_NAMES = submodule_name_map()

def dict_constructor(loader, node):
    return OrderedDict(loader.construct_pairs(node))

yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, dict_constructor)

def read_data_from_dir(path):
    date_str, title = path.split(' ', 1)
    date_obj = datetime.datetime.strptime(date_str, '%Y%m%d')
    with open(os.path.join(path, 'info.yaml'), 'r') as f:
        d = yaml.load(f)
    d.setdefault('audio', None)
    d.setdefault('video', None)
    d.setdefault('links', [])
    d['title'] = title
    d['date'] = date_obj.strftime('%B %d, %Y')
    d['date_obj'] = date_obj
    d['date_str'] = date_str
    d['formats'] = formats_at_path(path)
    if path in SUBMODULE_NAMES:
        d['github'] = 'http://www.github.com/hacsoc/{0}'.format(SUBMODULE_NAMES[path])
    else:
        d['github'] = 'http://www.github.com/hacsoc/talks/tree/master/{0}'.format(path)
    return d

def formats_at_path(path):
    formats = OrderedDict()
    for prespath in glob.glob(os.path.join(path, "presentation.*")):
        fmt = os.path.splitext(prespath)[1][1:]
        formats[fmt] = prespath
    return formats

def data_for_repos():
    unsorted_data = []
    for path in os.listdir('.'):
        if os.path.isdir(path) and path.startswith('2'):
            try:
                unsorted_data.append(read_data_from_dir(path))
            except IOError:
                print('{0} does not have an info.yaml file and will not appear on the page.'.format(path))

    key = lambda d: d['date_obj']
    return sorted(unsorted_data, key=key, reverse=True)

def render_talks(talks):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    t = env.get_template('template.html')
    with open('index.html', 'w') as f:
        f.write(t.render(talks=talks))

if __name__ == '__main__':
    render_talks(data_for_repos())
