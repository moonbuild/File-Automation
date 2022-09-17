#FIRST CHANGE THE PATH before beginning
folder = "/home/space-man/Downloads/"
documents = "/home/space-man/Documents/"
#[space-man is just my username]
import os
from pathlib import Path
import shutil

## U can experiment better with the below code!
### DONT FORGET TO REMOVE the next TWO lines of code when actually putting this to use.
for i in range(10):
    Path(folder+'snake🐍'+str(i)+'.py').touch()

def move(file_loc, path):
    os.makedirs(path, exist_ok=True)
    shutil.move(file_loc, path)

def sort():
    for file_name in os.listdir(folder):

        file_loc = folder+file_name

        if os.path.isdir(os.path.join(folder, file_name)):
            continue  

        if 'wall' in file_name:
            move(file_loc ,folder+'wallpaper/')

        if file_name.endswith('.py'):
            move(file_loc, folder+'Python files/')
        
        elif file_name.endswith('.jpeg') or file_name.endswith('.png') or file_name.endswith('.jpg'):
            move(file_loc, '/home/space-man/Pictures/')
        
        elif file_name.endswith('.txt'):
            move(file_loc, documents)
            
        elif file_name.endswith('.zip'):
            move(file_loc, folder+'Zip files/')

        elif file_name.endswith('pdf'):
            move(file_loc, documents)

        elif file_name.endswith('.csv'):
            move(file_loc, documents+'CSV Files/')

        else:
            move(file_loc, folder+'Other/')
            

if __name__ == '__main__':
    sort()
