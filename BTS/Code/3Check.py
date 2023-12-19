import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


img = Image.open('../../3:Q29sb3JCaXRDb2xsYWdl/3.png')
data = np.array(img)

#get the LSB of the all chanels and display it as an image

data2 = np.zeros((data.shape[0],data.shape[1],3),dtype="uint8")

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(data.shape[2]):
            data2[i, j, k] = 255* (data[i, j, k] %2)


    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))


T = Image.fromarray(data2)
T.show()


pass