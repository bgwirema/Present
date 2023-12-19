import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


img = Image.open("../../2:U29tZXRoaW5nVmlzdWFs/2.png")
data = np.array(img)

#get the LSB of the red chanel and display it as an image

data2 = np.zeros((data.shape[0],data.shape[1]),dtype="uint8")

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        data2[i, j] = 255* (data[i, j, 0] %2)


    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))


T = Image.fromarray(data2)
T.show()


pass