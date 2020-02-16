import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lab.jpg')
gray_img = cv2.imread('lab.jpg',0)
blur = cv2.GaussianBlur(gray_img, (1,1), 0)
ret, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Before', img)
cv2.imshow('After', th3)
cv2.waitKey(0)
