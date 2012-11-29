#!/usr/bin/python

#For convenience I add this to my .bashrc like so:
# alias 'rename'='~/rename.py'
# since i've put rename.py in my home dir

import os
import sys

print "renaming..."
src = sys.argv[1]
dst = sys.argv[2]
path = "."
for root, dirs, files in os.walk(path):
    if ".git" in dirs:
            dirs.remove(".git")
    for f in files:
        if f.startswith(src + "."):
            suffix = f.split(src)[1]
            srcf = os.path.join(path, f) 
            dstf = os.path.join(path, dst + suffix)
            os.rename(srcf, dstf)
            print "renamed", srcf, "to", dstf
            

        #print f.endswith(".meta"), f

