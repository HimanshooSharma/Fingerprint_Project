from PIL import Image, ImageEnhance
import os
import glob
import random
import numpy as np
from scipy.ndimage import rotate

#input images path
#pathin = "/Users/kanishk/Desktop/itsec"
pathin = "./in/"
#output images path
pathout = "./out/"
#background images path
pathbg = "./bg/"

out = 1
bg = 0
#bg1 = len(bgfiles)
backgroundIndex = 0
angles = np.array(range(30, 271,7))
BackgroundFilePathList = glob.glob('bg/*.jpg')

# for ImageFilePath in glob.glob('in/*.jpg'):
for ImageFilePath in glob.glob('fvc_in/*.tif'):
    img = None
    used_orientation = {}
    for k in range(5):
        if k > 0:
            if backgroundIndex < len(BackgroundFilePathList):
                background = Image.open(BackgroundFilePathList[backgroundIndex])
                backgroundIndex += 1
            else:
                backgroundIndex = 0
                background = Image.open(BackgroundFilePathList[backgroundIndex])
            # print(backgroundIndex)
            background = background.resize((512, 512), Image.ANTIALIAS)
            img = Image.open(ImageFilePath)
            img = img.convert("RGBA")
            img = ImageEnhance.Contrast(img)
            img = img.enhance(1.6)
            angle = random.choice(angles)
            while  True:
                if angle in used_orientation:
                    angle = random.choice(angles)
                else:
                    used_orientation.add(angle)
                    break
            
            img = img.rotate(angle, expand=True)
            # background.show()
            # quit()
        else:
            if backgroundIndex < len(BackgroundFilePathList):
                background = Image.open(BackgroundFilePathList[backgroundIndex])
                backgroundIndex += 1
            else:
                backgroundIndex = 0
                background = Image.open(BackgroundFilePathList[backgroundIndex])
            # print(backgroundIndex)
            background = background.resize((512, 512), Image.ANTIALIAS)
            img = Image.open(ImageFilePath)
            img = img.convert("RGBA")
            img = ImageEnhance.Contrast(img)
            img = img.enhance(1.6)

        datas = img.getdata()
        newData = []

        #making white background in impressions transparent
        for item in datas:
            if item[0] > 140 and item[1] > 140 and item[2] > 140:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        
        #pasting impressions on background image
        width = img.size[0]
        height = img.size[1]
        offset = (int(round(((512 - width) / 2), 0)), int(round(((512 - height) / 2),0)))
        # background.paste(img, offset, img)
        background.paste(img, offset, img)
        background.save(f'./fvc_out/{str(out)}.jpg')
        out += 1
        if not out%100:
            print(f'Generated {str(out)} images')
        # bg += 1
        # if bg == bg1:
        #     bg = 0
