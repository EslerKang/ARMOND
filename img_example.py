import cv2

img = cv2.imread("img/4.jpg", cv2.IMREAD_COLOR)

result = cv2.blur(img, (105,105), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)

result = cv2.resize(result, dsize=(640,480), interpolation=cv2.INTER_AREA)

cv2.imshow("Fruit", result)

cv2.waitKey(0)
cv2.destroyAllWindows()