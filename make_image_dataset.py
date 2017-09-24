import glob
import numpy as np
from PIL import Image

data_glob = './data/*tif'
out_file_name = 'images.npy'

def crop(input, height=128, width=128):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    crops = []
    for i in range(0, imgheight-height, height):
        for j in range(0, imgwidth-width, width):
            box = (j, i, j+width, i+height)
            c = im.crop(box)
            c = np.asarray(c, dtype=float)
            crops.append(c)
    return crops

crops = []
for file_name in glob.glob(data_glob):
	print('Croping file: %s' % (file_name))
	crops += crop(file_name)
data = np.array(crops)
print('Data min: %d\nData max: %d' % (data.min(), data.max()))
data -= data.min() # normalize between 0 and 1
data /= data.max()
print('Data shape: %s' % (str(data.shape)))
np.save(out_file_name, data)
