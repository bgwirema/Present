import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('../SourceFiles/picR.jpg')

data = np.array(img)


message = "{U29tZXRoaW5nVmlzdWFs}"

# encode the message in most significant bits on Pi's forehead

count = 0
ind = 0

for i in range(424,451):
    for j in range(288,800):
        for k in range(data.shape[2]):
            if count % 8 == 0:
                if ind>=len(message):
                    break
                c = ord(message[ind])
                ind += 1
                l = 2**7


            data[i, j, k] = data[i, j, k] - (data[i, j, k] // (2**7))*(2**7) + (c//l)*(2**7)
            c = c % l
            l = l // 2

            count += 1

    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))


T = Image.fromarray(data)
T.save("../../1:Tm90U29MZWFzdEJpdA/1.png")
T.show()


pass