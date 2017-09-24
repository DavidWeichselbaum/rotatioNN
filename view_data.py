import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


data = np.load(sys.argv[1])
for array in data:
	plt.imshow(array, cmap='gray', vmin=0, vmax=1)
	plt.colorbar()
	plt.draw()
	plt.pause(0.1)
	plt.clf()
