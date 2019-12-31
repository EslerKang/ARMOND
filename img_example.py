import cv2

img = cv2.imread("img/1.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Moon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()