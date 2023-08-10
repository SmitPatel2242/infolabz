import cv2
images=["images/1.webp","images/2.webp","images/3.jpeg","images/4.webp","images/5.jpeg","images/6.jpeg","images/7.webp","images/8.jpeg","images/9.jpeg","images/10.jpeg"]
path1 ="resize"
path2="blur"
path3="gray"
path4="edges"
for i in range(0,len(images)):
    image = cv2.imread(images[i])
    resizeimage = cv2.resize(image,(500,500))
    blurimage = cv2.GaussianBlur(resizeimage,(5,5),-5)
    grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(resizeimage,threshold1=100,threshold2=200)
    print(images[i])
    cv2.imwrite(path1+images[i],resizeimage)
    cv2.imwrite(path2+images[i],blurimage)
    cv2.imwrite(path3+images[i],grayimage)
    cv2.imwrite(path4+images[i],edges)
