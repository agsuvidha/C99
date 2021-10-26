import os
import shutil
path=input("Enter the path that needs to be sorted \n")
list=os.listdir(path)
print(list)

for file in list:
    name,ext=os.path.splitext(file)
    #print(name)
    #print(ext)
    
    ext=ext[1:]
    
    #print(ext[1:2])

    
    if ext=='':
        continue

    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    
