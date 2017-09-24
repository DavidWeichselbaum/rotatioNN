import glob
import numpy as np
from PIL import Image

data_glob = './data/*tif'
out_file_name = 'images.npy'

def crop(input, height=128, width=128):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    crops = []
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            c = im.crop(box)
            c = np.asarray(c)
            crops.append(c)
    return crops

crops = []
for file_name in glob.glob(data_glob):
	print('Croping file: %s' % (file_name))
	crops += crop(file_name)
data = np.array(crops)
print('Data shape: %s' % (str(data.shape)))
np.save(out_file_name, data)
