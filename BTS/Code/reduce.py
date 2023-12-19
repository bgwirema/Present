import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# literally just lowers the resolution of the picture you sent me lol

img = Image.open('../SourceFiles/pic.jpg')

data = np.array(img)
data2 = np.zeros((data.shape[0]//4,data.shape[1]//4,3),dtype='uint8')

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(data.shape[2]):
            if i%4 ==0 and j%4==0:
                data2[i//4,j//4,k] = data[i,j,k]
    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))

T = Image.fromarray(data2)
T.save("../SourceFiles/picR.jpg")
T.show()


pass