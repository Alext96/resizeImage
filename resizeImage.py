from PIL import Image
import os
import sys

path = "X:\\spreadshirtshirts\\testBatch\\"
dirs = os.listdir(path)
os.chdir(path)
print(dirs)
print(path)


def resize():
    for item in dirs:
        file = path + item
        if os.path.isfile(file):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((4500, 5400), Image.ANTIALIAS)
            imResize.save(f+'.png', 'png')

resize()
