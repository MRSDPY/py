import cv2

image = cv2.imread("aim.png")

resize = cv2.resize(image, (20, 20))

cv2.imshow("RS", resize)

cv2.imwrite("aim_r.png", resize)

cv2.waitKey(0)

cv2.destroyAllWindows()
