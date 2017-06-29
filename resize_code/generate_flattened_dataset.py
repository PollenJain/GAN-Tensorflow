import os
import cv2
import numpy as np

dataset = np.arange(784).reshape((1,784))
for imageName in os.listdir('/home/paragjain/Desktop/GAN Trial/resize_code/ALL_RESIZED'):
	image = cv2.imread('/home/paragjain/Desktop/GAN Trial/resize_code/ALL_RESIZED/'+imageName, 0)
	image_flattened = image.flatten()
	print(image_flattened.shape)
	dataset = np.vstack((dataset, image_flattened))
	

dataset = np.delete(dataset, 0, axis=0)
print(dataset.shape)
