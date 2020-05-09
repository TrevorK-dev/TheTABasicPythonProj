import os, sys
dirs = os.listdir( "C:\A" )

print( "C:\A" )

abspath = os.path.join("C:\A","Hello.txt")

print(abspath)


os.path.getmtime( "C:\A" )
