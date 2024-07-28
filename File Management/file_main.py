import shutil
import os

path = input("Enter the Path: ")
files = os.listdir(path)
print(files)

for file in files:
  filename, extension = os.path.splitext(file)
  extension = extension[1:]

  if os.path.exists(path+'/'+extension):
    shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
  else:
    os.makedirs(path+'/'+extension)
    shutil.move(path+'/'+file, path+'/'+extension+'/'+file)