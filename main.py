import shutil
import os

files = os.listdir()

os.mkdir("Images")
os.mkdir("Videos")
os.mkdir("Documents")
os.mkdir("Music")
os.mkdir("Archives")

for file in files:
    if(file.endswith(".mp4")):
        shutil.move(file,"Videos")
    if(file.endswith(".jpg")):
        shutil.move(file,"Images")
    if(file.endswith(".pdf")):
        shutil.move(file,"Documents")
    if(file.endswith(".mp3")):
        shutil.move(file,"Music")
    if(file.endswith(".zip")):
        shutil.move(file,"Archives")