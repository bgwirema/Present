import random

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('../SourceFiles/picR.jpg')
flagImg = Image.open('../SourceFiles/4:flag.jpg')

data = np.array(img)
flagData = np.array(flagImg)


# add noise to the last 3 bits of all channels
# if it's a flag pixel make the last the bits either all on or all off

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(data.shape[2]):
            data[i, j, k] = data[i, j, k] & (2 ** 8 - 2 ** 3)
            if (flagData[i,j,k]//128)==0:
                data[i,j,k] += 7*random.randint(0,1)
            else:
                for b in range(3):
                    data[i, j, k] += (2**b) * random.randint(0, 1)


    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))


T = Image.fromarray(data)
T.save("../../4:VG83T3JOb3RUbzc/4.png")
T.show()


pass