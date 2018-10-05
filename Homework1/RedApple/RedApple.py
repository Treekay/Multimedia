from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt
import operator
import cv2

def ImgProcess(img):
    rows, cols, dims = img.shape
    R, G, B = 0, 1, 2
    pixels = []

    # pick up all the pixels
    for x in range(rows):
        for y in range(cols):
            pixels.append([img[x,y,R],img[x,y,G],img[x,y,B],x,y])

    # determine the 256 present color
    medianNum = len(pixels)
    pixels.sort(key=operator.itemgetter(R))
    for t in range(8):
        medianNum = medianNum//2
        ltimes = len(pixels) // medianNum
        if (t%3 == 0):
            for i in range(ltimes):
                pixels[i*medianNum:(i+1)*medianNum].sort(key=operator.itemgetter(R))
        elif (t%3 == 1):
            for i in range(ltimes):
                pixels[i*medianNum:(i+1)*medianNum].sort(key=operator.itemgetter(G))
        elif (t%3 == 2):
            for i in range(ltimes):
                pixels[i*medianNum:(i+1)*medianNum].sort(key=operator.itemgetter(B))

    region = len(pixels)//256
    for t in range(256):
        medianColor = pixels[(2*t+1)*region//2]
        for i in range(t*region,(t+1)*region):
            x = pixels[i][3]
            y = pixels[i][4]
            img[x,y,R] = medianColor[R]
            img[x,y,G] = medianColor[G]
            img[x,y,B] = medianColor[B]

    # show and save the new img
    img = Image.fromarray(np.uint8(img))
    plt.figure(2)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None) # 去除白边
    plt.imshow(img)
    plt.axis('off')
    plt.savefig("../img/hw2.jpg")
    plt.show()

# main()
image = Image.open('../img/redapple.jpg')
img = np.array(image)
plt.figure(1)
plt.imshow(img)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None) # 去除白边
plt.axis('off') # 去除坐标系
ImgProcess(img)