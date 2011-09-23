from collections import OrderedDict
import datetime
import glob
import os
import re
import sys

import jinja2
import yaml

GIT_RE = re.compile(r'\s+url = git://github.com/hacsoc/(?P<name>.*)\.git\n')
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

unsorted_data = {}
for path in os.listdir('.'):
    if os.path.isdir(path) and path.startswith('2'):
        date_str, title = path.split(' ', 1)
        date = datetime.datetime.strptime(date_str, '%Y%m%d').strftime('%B %d, %Y')
        try:
            with open(os.path.join(path, 'info.yaml')) as f:
                d = yaml.load(f)
                unsorted_data[path] = d
                d['title'] = title
                d['date'] = date
                d.setdefault('audio', None)
                d.setdefault('video', None)
                d['formats'] = OrderedDict()
                for prespath in glob.glob(os.path.join(path, "presentation.*")):
                    fmt = os.path.splitext(prespath)[1][1:]
                    d['formats'][fmt] = os.path.join(path, prespath)
                if path in submodules:
                    d['github'] = 'http://www.github.com/hacsoc/{0}'.format(submodules[path])
                else:
                    d['github'] = 'http://www.github.com/hacsoc/talks/tree/master/{0}'.format(path)
        except IOError:
            print('{0} does not have an info.yaml file and will not appear on the page.'.format(path))

sorted_data = [unsorted_data[k] for k in sorted(unsorted_data.keys(),
                                                key=lambda d: unsorted_data[d]['title'])]

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
t = env.get_template('template.html')
with open('index.html', 'w') as f:
    f.write(t.render(talks=sorted_data))
