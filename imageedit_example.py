import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("img/4.jpg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()


cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())

cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(img2),plt.title('Equalization')
plt.show()