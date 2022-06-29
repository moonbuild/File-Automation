folder = "/home/dude/Downloads/Projects/Automation/THE FOLDER/"
import os
from pathlib import Path
import shutil


def Automate(file_name, ext, name):
    if file_name.endswith("."+ext):
        p = Path(folder+name)
        p.mkdir(exist_ok = True)
        shutil.move(folder+file_name, folder+name)

def sort():
    for file_name in os.listdir(folder):
        Automate(file_name,"py", "Snake Files")
        Automate(file_name,"pdf", "Papers")
        Automate(file_name,"jpeg", "Pictures")
        Automate(file_name,"png", "Pictures")
        Automate(file_name,"txt", "Ideas")
        Automate(file_name,"mp3", "Songs")

if __name__ == '__main__':
    sort()