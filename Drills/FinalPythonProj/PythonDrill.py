import os, sys
path = "C:\A"
dirs = os.listdir( path )
print(dirs)

for x in dirs:
    if x.endswith(".txt"):
        abspath = os.path.join(path, x)
        print(abspath)
        gmtime = os.path.getmtime( abspath )
        print(gmtime)
    


##print(abspath)


##os.path.getmtime( "C:\A" )

##os.path.join("C:\A", "Hello.txt")

##for os.listdir( path ) = ".txt":
    
