import os

for f in os.listdir("./photos"):
    r = f.replace(" ","")
    if( r != f):
        os.rename("./photos/"+f,"./photos/"+r)
        