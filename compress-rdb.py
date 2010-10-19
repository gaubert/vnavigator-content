#!/usr/bin/python
""" Compress all files in a RDB """

import os
import sys
import tarfile
import shutil

usage = "Usage:\n$>compress-rdb.py RDB-ROOT-DIR\n"

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

DIR="./VNAVIGATOR-RDB"

files=os.listdir(DIR)

print("list of potential dirs to backup: %s\n" %(files))

#change dir to DIR
os.chdir(DIR)

for the_file in files:

   if not the_file.endswith('.tgz'):
      print("Compress %s\n" % (the_file))
      targetBackup = '%s.tgz' % (os.path.basename(the_file))    
      print("---- tar gzip the following dir %s\n" % (the_file))
      tar = tarfile.open(targetBackup, "w:gz")
      tar.add('%s' % (the_file))
      tar.close()
      #delete the tarred dir
      print("---- delete %s\n" % (the_file))
      shutil.rmtree(the_file)
   else:
      print("%s already compressed\n" %(the_file))
      
