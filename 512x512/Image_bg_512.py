from PIL import Image
import glob
import traceback
from colorama import Fore, Style

def Reformat_Image(ImageFilePath,out_count):
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    try:
        square_side = 512

        background = Image.new('RGBA', (square_side, square_side), (255, 255, 255, 255))
        offset = (int(round(((square_side - width) / 2), 0)), int(round(((square_side - height) / 2),0)))

        background.paste(image, offset)
        rgb_background = background.convert('RGB')
        rgb_background.save(f'out/{str(out_count)}.jpg')
        if out_count % 100 == 0:
            print(f'{Fore.BLUE}Done with {str(out_count)} {Style.RESET_ALL}')
    except :
        print(f'{Fore.RED}Exception !!{Style.RESET_ALL}')
        traceback.print_exc()

if __name__ == "__main__":
    out_count = 0
    for ImageFilePath in glob.glob('in/*.jpg'):
        out_count += 1
        Reformat_Image(ImageFilePath,out_count)
