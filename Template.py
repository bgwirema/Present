import numpy as np
from PIL import Image

# path to the image
path = "./2:U29tZXRoaW5nVmlzdWFs/2.png"


# put the pixel data in to a numpy array
img = Image.open(path)
data = np.array(img)


# create new array to put the modified image into
data2 = np.zeros((data.shape[0],data.shape[1],3),dtype="uint8")


# loop through the pixels
for i in range(data.shape[0]):  # col
    for j in range(data.shape[1]):  # row
        for k in range(data.shape[2]):  # color
            # do stuff

            # example: get only the red chanel
            if k==0:
                data2[i,j,k] = data[i,j,k]


#show the new image you made
Image.fromarray(data2).show()


pass