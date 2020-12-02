from PIL import Image
import os

#input images path
pathin = "C:\\Users\\Atif\\Desktop\\New folder\\Input\\"
#output images path
pathout = "C:\\Users\\Atif\\Desktop\\New folder\\Output\\"
#background images path
pathbg = "C:\\Users\\Atif\\Desktop\\New folder\\bg\\"


#reading all input images filenames
imgfiles = [f for f in os.listdir(pathin) if os.path.isfile(os.path.join(pathin, f))]
#reading all background images filenames
bgfiles = [f for f in os.listdir(pathbg) if os.path.isfile(os.path.join(pathbg, f))]

bg = 0
bg1 = len(bgfiles)

for i in imgfiles:
    img = Image.open(pathin + i)
    img = img.convert("RGBA")
    background = Image.open(pathbg + bgfiles[bg])
    background = background.resize((512, 512), Image.ANTIALIAS)
    datas = img.getdata()
    newData = []
    #making white background in impressions transparent
    for item in datas:
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    #pasting impressions on background image
    background.paste(img, (0, 0), img)
    background.save(pathout + i, "JPEG")
    bg += 1
    if bg == bg1:
        bg = 0








