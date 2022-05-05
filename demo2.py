import os
import shutil

path='folder_a'
print("Before copying")
print(os.listdir(path))

source='folder_a/bird.png'
dest='folder_b/bird.png'

do=shutil.move(source,dest)

