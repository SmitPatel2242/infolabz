import cv2

image = ["1.webp","2.webp","3.jpeg","4.webp","5.jpeg","6.jpeg","7.webp","8.jpeg","9.jpeg","10.jpeg"]
type = ["blur","resize","edges","gray"]



for i in image:
    read = cv2.imread("images/"+i)
    resizeimage = cv2.resize(read,(500,500))
    blurimage = cv2.GaussianBlur(resizeimage,(5,5),-5)
    grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(resizeimage,threshold1=100,threshold2=200)
    
    cv2.imwrite("image/blur/"+i,blurimage)
    cv2.imwrite("image/edges/"+i,edges)
    cv2.imwrite("image/gray/"+i,grayimage)
    cv2.imwrite("image/resize/"+i,resizeimage)

print("Image Stored Successfully")