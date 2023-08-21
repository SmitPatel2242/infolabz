import cv2
import numpy as np

image = 255 * np.ones((400,600,3) , dtype=np.uint8)
cv2.line(image,(50,100),(100,100),(0,0,255),2)
cv2.rectangle(image,(100,200),(200,230),(0,255,0),-3)
cv2.circle(image,(200,200),50,(255,0,0),2)
cv2.putText(image,"SMIT",(100,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()