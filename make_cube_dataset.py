import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import matplotlib.pyplot as plt
import random
from PIL import Image

n_samples = 10000
width, heigth = 64, 64
tmp_file_name = '.tmp.png'
out_file_name = 'cubes.npy'

points = np.array([[-10, -1, 0],
                  [  1, -1, 0 ],
                  [  5,  1, 0],
                  [ -1,  1, 0],
                  [ -10, -1, 1],
                  [  1, -1, 1 ],
                  [  5,  1, 1],
                  [ -1,  1, 1]])

P = [[2.06498904e-01 , -6.30755443e-07 ,  1.07477548e-03],
 [1.61535574e-06 ,  1.18897198e-01 ,  7.85307721e-06],
 [7.08353661e-02 ,  4.48415767e-06 ,  2.05395893e-01]]

Z = np.zeros((8,3))
for i in range(8): Z[i,:] = np.dot(points[i,:],P)
Z = 10.0*Z

fig = plt.figure()
fig.set_size_inches(width, heigth)
ax = fig.add_subplot(111, projection='3d')

r = [-1,1]

X, Y = np.meshgrid(r, r)
# plot vertices
ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2], s=0) # no point

# list of sides' polygons of figure
verts = [[Z[0],Z[1],Z[2],Z[3]],
 [Z[4],Z[5],Z[6],Z[7]], 
 [Z[0],Z[1],Z[5],Z[4]], 
 [Z[2],Z[3],Z[7],Z[6]], 
 [Z[1],Z[2],Z[6],Z[5]],
 [Z[4],Z[7],Z[3],Z[0]], 
 [Z[2],Z[3],Z[7],Z[6]]]

# plot sides
ax.add_collection3d(Poly3DCollection(verts, facecolors='white', linewidths=30, edgecolors='black', alpha=0))
ax.set_facecolor((0, 0, 0))
plt.axis('off')
plt.tight_layout()

# for i in range(0, 360, 30):
# 	for j in range(0, 360):
# 		ax.view_init(i, j)
# 		plt.draw()
# 		plt.pause(.001)
# exit(0)

data = []
for i in range(n_samples):
	angle = random.random() * 360
	azimuth = random.random() * 360
	print('Generating data point %d   %2.2f   %2.2f' % (i+1, angle, azimuth), end='\r')
	ax.view_init(azimuth, angle)
	fig.savefig(tmp_file_name, dpi=1) # ugly, I know, but more robust than the alternative 
	img = Image.open(tmp_file_name).convert('L') # grayscale
	img.load()
	array = np.asarray(img, dtype="int32")
	data.append(array)
data = np.array(data, dtype=float)
data /= 255
print('\nData shape: %s' % (str(data.shape)))
np.save(out_file_name, data)
