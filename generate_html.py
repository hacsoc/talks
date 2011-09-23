import datetime
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
                unsorted_data[path] = yaml.load(f)
                unsorted_data[path]['title'] = title
                unsorted_data[path]['date'] = date
        except IOError:
            print('{0} does not have an info.yaml file and will not appear on the page.'.format(path))

sorted_data = {k: unsorted_data[k] for k in sorted(unsorted_data.keys())}

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

t = env.get_template('template.html')

with open('index.html', 'w') as f:
    f.write(t.render(talks=sorted_data))
