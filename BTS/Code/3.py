import matplotlib.pyplot as plt
import random
import numpy as np
from PIL import Image

img = Image.open('../SourceFiles/picR.jpg')
flagImg = Image.open('../SourceFiles/3:flag.jpg')

data = np.array(img)
flagData = np.array(flagImg)




for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        k = random.randint(0,2)
        data[i, j, k] = data[i, j, k] - data[i, j, k]%2 + (flagData[i,j,k] // 128)


    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))


T = Image.fromarray(data)
T.save("../../3:Q29sb3JCaXRDb2xsYWdl/3.png")
T.show()


pass