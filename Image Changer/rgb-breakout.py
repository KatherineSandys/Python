import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

file_name = "Image Changer/cars.jpg"

img = mpimg.imread(file_name)
r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

'''
plt.imshow(r, cmap="Reds")
plt.show()
plt.imshow(g, cmap ="Greens")
plt.show()
plt.imshow(b, cmap="Blues")
plt.show()
'''

rgb_list = ['Reds','Greens','Blues']
fig, ax = plt.subplots(1, 3, figsize=(15,5), sharey = True)
for i in range(3):
    ax[i].imshow(img[:,:,i], cmap = rgb_list[i])
    ax[i].set_title(rgb_list[i], fontsize = 15)

fig.show()