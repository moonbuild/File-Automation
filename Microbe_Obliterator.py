folder = "/home/dude/Downloads/"
import os
from pathlib import Path
import shutil


def Automate(file_name, name, path=False):
    if path==True:
        p = Path(name)
        p.mkdir(exist_ok = True)
        print(folder+file_name)
        print(name)
        shutil.copy(folder+file_name, name)
    else:
        p = Path(folder+name)
        p.mkdir(exist_ok = True)
        shutil.move(folder+file_name, folder+name)


def sort():
    for file_name in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, file_name)):
            continue
        elif file_name == 'Microbe_Obliterator.py':
            continue   

        elif file_name.endswith('.py'):
            Automate(file_name, 'Python files')

        elif file_name.endswith('.sol'):
            Automate(file_name, 'Solidity_files')

        elif file_name.endswith('.zip'):
            Automate(file_name, 'Zip files')

        elif file_name.endswith('pdf'):
            Automate(file_name, '/home/dude/Documents/', path=True)
        elif file_name.endswith('.csv'):
            Automate(file_name, '/home/dude/Documents/CSV Files')
        elif file_name.endswith('.txt'):
            Automate(file_name, '/home/dude/Documents/', path=True)
            
        elif file_name.endswith('.jpeg') or file_name.endswith('.png') or file_name.endswith('.jpg'):
            Automate(file_name, '/home/dude/Pictures/', path=True)

        else:
            Automate(file_name, 'Other')
            

if __name__ == '__main__':
    sort()
