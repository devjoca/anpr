import cv2
import numpy as np

#image equalization
img = cv2.imread('images/image.png',0)
equ = cv2.equalizeHist(img)
#gauss blur
gauss = cv2.GaussianBlur(equ,(5,5),0)
#get edges
edges = cv2.Canny(gauss,100,200)
cv2.imwrite('out/edges-gaus.png',edges)
