import os
os.system("date")

os.mkdir("c://users/Suvidha/desktop/pytho")
os.getcwd()

path='c://users/Suvidha/desktop/pyth'
isExist=os.path.exists(path)
print(isExist)

path2='c://users/suvidha/desktop/file.txt'
root_ext=os.path.splitext(path2)
print("root is "+root_ext[0])
#root is c://users/suvidha/desktop/file
print("ext is "+root_ext[1])
#ext is .txt

os.listdir()

path='c://users/Suvidha/desktop'
os.listdir(path)

