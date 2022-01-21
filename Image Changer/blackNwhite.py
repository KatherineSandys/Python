from PIL import Image

from matplotlib import pyplot as plt
import matplotlib.image as mpimg

print("\nblack and white conversion of images")

#get the file name from the user
#file_name = input("Enter the file name and or path to the image: ")
file_name = "Image Changer/flowers.PNG"

#open the file
img = Image.open(file_name, "r")

#transition it to gray scale
#first way
imgGray = img.convert('L')
imgGray.save('changed.PNG')

#second way
img = mpimg.imread(file_name)
r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]
imgGray = 0.3 * r + 0.6 * g + 0.1 * b
plt.imshow(imgGray, cmap='gray')
plt.show()