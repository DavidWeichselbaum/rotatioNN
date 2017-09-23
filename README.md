# rotatioNN

Extracting the 3D structure of a protein from a set of electron microscopy images is callenging.
Not only are instances of the protein captured from all possible angles, they also differ between each other because of their intrinsic dynamics.

Current approaches involve sorting a large number of noisy protein shapes into similar categories and inferring structure from a cummulation of those.
Here, I try to do something not entirely unsimilar, by using a variational autencoder. 
The idea is to compress a set of images to a vector of a given size, which necessarily encodes rotation and translation, but also dynamics.

The encluded toy example generates a dataset of snapshots of random rotations of a prisma in two dimensions.
Since those rotations are all the data needed to reconstruct any given image, an autoencoder trained to compress such an image into a two-dimensional vector will necessarily encode this rotation.
Since it's an Variational Autoencoder, two vectors generated by rotated objects close to each other in this rotation, will be close in the encoded vector as well.
Therefore we can sample from the encoded vector to visualize rotation in the dataset:

![Sampling a two-dimensional vector to generate rotated prisms.](https://user-images.githubusercontent.com/22052799/30777151-ef82ab26-a0b4-11e7-9292-88d18a14c05a.png)

To generate the toy data, do:

> python3 make_cube_dataset.py

To run the training and evaluation, do:

> python3 variational_autoencoder.py

The autoencoder model used is directly from the [Keras Examples](https://github.com/fchollet/keras/blob/master/examples/variational_autoencoder.py).