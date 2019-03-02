from PIL import Image
import matplotlib.image as img
import os
import numpy as np

DIR_CURRENT = os.path.dirname(os.path.realpath(__file__))
DIR_IMG_FORMAT = '{}/pics/einstein_format'.format(DIR_CURRENT)

def getMatrix():
    images = [
        '{}/{}'.format(DIR_IMG_FORMAT,file)
        for file in os.listdir(DIR_IMG_FORMAT) if file[-3:].lower()=='png'
    ]
    data = []
    for image in images:
        # print(image)
        data_sub = img.imread(image)
        if len(data_sub.shape)>2:
            data_sub = data_sub.mean(axis=2)
            # print(data_sub.shape)
        # flatten the 2d array to 1d
        data.append(data_sub.ravel())
    data = np.array(data)
    print(data.shape)
    return(data)

if __name__ == '__main__':
    getMatrix()