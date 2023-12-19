import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('../SourceFiles/picR.jpg')

data = np.array(img)


message = "{https://filebin.net/Tm90U29MZWFzdEJpdA}"

# LSB embedding

count = 0
ind = 0

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(1):
            if count % 8 == 0:
                if ind>=len(message):
                    break
                c = ord(message[ind])
                ind += 1
                l = 2**7


            data[i, j, k] = data[i, j, k] - data[i, j, k] % 2 + c // l
            c = c % l
            l = l // 2

            count += 1

    if i % (data.shape[0] // 20) == 0:
        print("{percent:.1f}%".format(percent=i / data.shape[0] * 100))


T = Image.fromarray(data)
T.save("../../0:email/0.png")
T.show()


pass