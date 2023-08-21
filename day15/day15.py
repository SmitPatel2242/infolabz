import cv2

image = cv2.imread("shape.jpeg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
edges = cv2.Canny(blur,50,150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    ep = 0.04 * cv2.arcLength(contour,True)
    approx = cv2.approxPolyDP(contour,ep,True)
    numv = len(approx)

    if numv==3:
        shapename = "Triangle"
    elif numv==4:
        shapename = "Rectangle"
    elif numv==5:
        shapename = "Pentagon"
    elif numv==6:
        shapename = "Hexagon"
    else:
        shapename = "circle"

    cv2.drawContours(image,[contour],-1,(0,0,0),2)
    x,y = contour[0][0]
    cv2.putText(image,shapename,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)

cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()