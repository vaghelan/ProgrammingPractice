

import sys

import os

import glob

import fnmatch, re

files_path = sys.argv[1]
fp = open(sys.argv[2], "w")

#matches = []
for root, dirnames, filenames in os.walk(files_path):
    for filename in fnmatch.filter(filenames, '*.csv'):
        print os.path.join(root, filename)
        #matches.append(os.path.join(root, filename))
        fp.write(os.path.join(root, filename) + "\n")
        fp.flush()

fp.close()

sys.exit(0)





