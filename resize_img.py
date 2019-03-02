from PIL import Image
import os

DIR_CURRENT = os.path.dirname(os.path.realpath(__file__))
DIR_IMG_RAW = '{}/pics/einstein_raw'.format(DIR_CURRENT)
def resize(path_in):
    img = Image.open(path_in)
    new_img = img.resize((100,100))
    path_out = '{}/pics/einstein_format/{}'.format(DIR_CURRENT,path_in.split('/')[-1])
    new_img.save(path_out, "png", optimize=True)

def main():
    images = [
        '{}/{}'.format(DIR_IMG_RAW,file)
        for file in os.listdir(DIR_IMG_RAW)
    ]
    for image in images:
        resize(image)

if __name__ == '__main__':
    main()