import os, sys

path = "C:\A"
dirs = os.listdir( path )

print(path)

os.path.getmtime(path)

abspath = os.path.join(path,"Hello.txt")

print(abspath)
