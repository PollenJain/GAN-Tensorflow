import os
import cv2

destPath = '/home/paragjain/Desktop/GAN Trial/resize_code/ALL_RESIZED'


if not os.path.exists(destPath):
	os.makedirs(destPath)

count = 0
images = []

for root, subdirs, files in os.walk('./input_images'):
	if files:
		print(root)
		path = root + "/"
		images.extend([path+image_name for image_name in files])


for imagePath in images:
	image = cv2.imread(imagePath,0)
	image_resized = cv2.resize(image, (28, 28), interpolation = cv2.INTER_CUBIC)
	cv2.imwrite(destPath+"/train_"+str(count)+".jpeg", image_resized)
	count = count + 1
