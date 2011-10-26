#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Tim Henderson
# Email: tim.tadh@hackthology.com
# This file is in the Public Domain

import os, sys, threading, itertools, time
from hashlib import sha256

PASSWORD = sha256('security').digest()

def file_or_die(path):
    if not os.path.exists(path):
        sys.stderr.write("Could not find the file %s\n" % os.path.abspath(path))
        sys.exit(1)
    f = open(path, 'r')
    s = f.read()
    f.close()
    return s

def check(d):
    if PASSWORD in d:
        print 'Found password it was "%s"' % d[PASSWORD]
        sys.exit(0)

class worker(threading.Thread):

    def __init__(self, words, done):
        self.words = words
        self.done = done
        super(worker, self).__init__()

    def run(self):
        d = dict()
        for word in self.words:
            d[sha256(word).digest()] = word
        self.done(d)

def chunks(l, n):
    """ Yield successive n-sized chunks from l.  """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

words = [
    line.strip() 
    for line in file_or_die('./dictionary').split('\n')
    if line
]

work = chunks(words, 10)
threads = [worker(item, check) for item in work]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join(10)

