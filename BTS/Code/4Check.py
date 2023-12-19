import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


img = Image.open("../../4:VG83T3JOb3RUbzc/4.png")
data = np.array(img)

# display the last the bits of any color chanel as RGB
# black and white squares are the flag, colored are not

data2 = np.zeros((data.shape[0],data.shape[1],3),dtype="uint8")

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        data2[i,j,0] = ((data[i,j,0]&1)>0)* 255
        data2[i, j, 1] = ((data[i,j,0]&2)>0)* 255
        data2[i, j, 2] = ((data[i,j,0]&4)>0)* 255



    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))


T = Image.fromarray(data2)
T.show()


pass