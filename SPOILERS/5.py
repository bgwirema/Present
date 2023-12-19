import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('../BTS/SourceFiles/pic.jpg')

data = np.array(img)

# LSB embedding the first ~3 million digits of pi

with open("ANumber.txt") as f:
    count = 0

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                if count%8 == 0:
                    if count//8 == 0:
                        c = ord('3')
                    elif count//8 == 1:
                        c = ord('.')
                    else:
                        c = ord(f.read(1))
                    l=2**7


                data[i,j,k] = data[i,j,k] - data[i,j,k]%2 + c//l
                c = c%l
                l = l//2

                count += 1
        if i%(data.shape[0]//20) == 0:
            print("{percent:.1f}%".format(percent=i/data.shape[0]*100))

T = Image.fromarray(data)
T.save("../5:UGlGb3JQaTop/pi.png")
T.show()


pass