from collections import OrderedDict
import datetime
import glob
import os
import sys

import jinja2
import yaml

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
        except IOError:
            print('{0} does not have an info.yaml file and will not appear on the page.'.format(path))

sorted_data = OrderedDict((k, unsorted_data[k]) for k in sorted(unsorted_data.keys()))

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
t = env.get_template('template.html')
with open('index.html', 'w') as f:
    f.write(t.render(talks=sorted_data))
