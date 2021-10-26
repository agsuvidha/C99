import os
import shutil
source=input("enter source folder")
dest=input("enter destination folder")

source=source+'/'
dest=dest+'/'

list=os.listdir(source)

for file in list:
    shutil.copy((source+file),dest)
