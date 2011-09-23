import os
import sys
import yaml

data = []
for path in os.listdir('.'):
    if os.path.isdir(path) and path.startswith('2'):
        try:
            with open(os.path.join(path, 'info.yaml')):
                pass
        except IOError:
            print('{0} does not have an info.yaml file and will not appear on the page.'.format(path))
