import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/image.png',0)

equ = cv2.equalizeHist(img)
gauss = cv2.GaussianBlur(equ,(5,5),0)
ret3, th2 = cv2.threshold(gauss,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# edges = cv2.Canny(th,100,200)

plt.imshow(th2, 'gray')
plt.show()