import os, sys
path = "C:\A"
dirs = os.listdir( path )
##print(dirs)

for x in dirs:
    if x.endswith(".txt"):
        abspath = os.path.join(path, x)
        print(abspath)
        gmtime = os.path.getmtime( abspath )
       print(gmtime)



##with moveshutil() get abs path, have that be the first arg for the move function.
##second arg will be curdirectory2  - destination , wont need abs path, just need path
##    for directory, no files names.
##
##Get functions for tkinter, assign new variable,
##x = self.text_filedir.get() - getting 2 dirs from 2 functions.  
    


##print(abspath)


##os.path.getmtime( "C:\A" )

##os.path.join("C:\A", "Hello.txt")

##for os.listdir( path ) = ".txt":
    
