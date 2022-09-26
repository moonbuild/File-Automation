#FIRST CHANGE THE PATH before beginning
folder = "/home/space-man/Downloads/"
documents = "/home/space-man/Documents/"
#[space-man is just my username]
"""
CRONTAB
*/5 * * * * python /home/space-man/Microbe_Obliterator.py
"""
import os
from pathlib import Path
import shutil

def join(a,b):
    return os.path.join(a,b)



def EVE(file_loc, dst_path):
    try:
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        shutil.move(file_loc, dst_path)

    except shutil.Error:
        files = os.scandir(folder)
        for file_name in files:
            file_name = file_name.name
            if os.path.isdir(join(folder, file_name)):
                continue
            src = join(folder, file_name)
            i=0
            while True:
                base = os.path.basename(src)
                name = f'-{i}'.join(os.path.splitext(base)) if i!=0 else base
                dst_loc = join(dst_path, name)
                if not os.path.exists(dst_loc):
                    shutil.move(src, dst_loc)
                    break
                i+=1
    

def WallE():
    for file_name in os.listdir(folder):

        file_loc = join(folder,file_name)

        if os.path.isdir(file_loc):
            continue  
        if 'wall' in file_name:
            EVE(file_loc ,join(folder+'wallpaper/'))

        if file_name.endswith('.py'):
            EVE(file_loc, join(folder,'Python files/'))
        
        if file_name.endswith('.txt'):
            EVE(file_loc, documents)

        elif file_name.endswith('.jpeg') or file_name.endswith('.png') or file_name.endswith('.jpg'):
            EVE(file_loc, '/home/space-man/Pictures/')
        
            
        elif file_name.endswith('.zip'):
            EVE(file_loc, join(folder,'Zip files/'))

        elif file_name.endswith('pdf'):
            EVE(file_loc, documents)

        elif file_name.endswith('.csv'):
            EVE(file_loc, join(documents,'CSV Files/'))

        else:
            EVE(file_loc, join(folder+'Other/'))
            

if __name__ == '__main__':
    WallE()
