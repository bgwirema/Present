import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('../SourceFiles/picR.jpg')
flagImg = Image.open('../SourceFiles/2:flag.jpg')

data = np.array(img)
flagData = np.array(flagImg)


# encode the flag image into the LSB of the red chanel

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        data[i, j, 0] = data[i, j, 0] - data[i, j, 0]%2 + (1 - (flagData[i,j,0] %2))


    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))


T = Image.fromarray(data)
T.save("../../2:U29tZXRoaW5nVmlzdWFs/2.png")
T.show()


pass