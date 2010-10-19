#!/usr/bin/python
""" Compress all files in a RDB """

import os
import tarfile
import shutil
import sys

usage = "Usage:\n$>uncompress-rdb.py RDB-ROOT-DIR\n"

if len(sys.argv) != 2:
   print("Error need 1 argument\n")
   print(usage)
   exit(1)

DIR=sys.argv[1]

if not os.path.exists(DIR):
   print("Error dir %s doesn't exist\n" %(DIR))
   print(usage)
   exit(1)

if not os.path.isdir(DIR):
   print("Error %s is not a dir\n" %(DIR))
   print(usage)
   exit(1)

files=os.listdir(DIR)
files.sort()
files.reverse()

print("list of potential dirs to uncompress: %s\n" %(files))

#dummy algo that will uncompress the last compressed dir

#go to DB dir
os.chdir(DIR)

extracted_last_file = False

for filename in files:

   if filename.endswith('.tgz'):
      print("Found %s to uncompress\n" % (filename))
      tar = tarfile.open(filename)   
      print("---- Uncompress %s\n" % (filename)) 
      tar.extractall()
      tar.close()
      extracted_last_file = True 
      print("---- Delete %s\n" % (filename))
      os.remove(filename)

   if extracted_last_file:
      break

print("RDB %s seems to be uncompressed\n" %(DIR)) 
