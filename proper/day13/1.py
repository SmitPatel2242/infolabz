import cv2

image = cv2.imread("yogi.png")
resizeimage = cv2.resize(image,(500,500))
blurimage = cv2.GaussianBlur(resizeimage,(5,5),-5)
grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(resizeimage,threshold1=150,threshold2=300)
# cv2.imshow("Image",resizeimage)
# cv2.imshow("ImageB",blurimage)
# cv2.imshow("ImageG",grayimage)
cv2.imshow("ImageE",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()