import cv2
import os
images=["1.webp","2.webp","3.jpeg","4.webp","5.jpeg","6.jpeg","7.webp","8.jpeg","9.jpeg","10.jpeg"]
# images=["1.jpeg","2.jpeg","3.jpeg","4.jpeg","5.jpeg","6.jpeg","7.jpeg","8.jpeg","9.jpeg","10.jpeg"]
# os.chdir("./images")
# image = cv2.imread(images[0])
# resizeimage = cv2.resize(image,(500,500))
# grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
# os.chdir("../gray")
# cv2.imwrite(images[0],grayimage)
path1 ="../resize"
path2="../blur"
path3="../gray"
path4="../edges"
os.mkdir("resize")
os.mkdir("blur")
os.mkdir("gray")
os.mkdir("edges")
os.chdir("./images")

for i in range(0,len(images)):

    image = cv2.imread(images[i])
    resizeimage = cv2.resize(image,(500,500))
    blurimage = cv2.GaussianBlur(resizeimage,(5,5),-5)
    grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(resizeimage,threshold1=100,threshold2=200)
    os.chdir(path1)
    cv2.imwrite(images[i],resizeimage)
    os.chdir(path2)
    cv2.imwrite(images[i],blurimage)
    os.chdir(path3)
    cv2.imwrite(images[i],grayimage)
    os.chdir(path4)
    cv2.imwrite(images[i],edges)
    os.chdir("../images")


############## 2nd way ######################


# for i in range(0,len(images)):
#
#     image = cv2.imread(images[i])
#     resizeimage = cv2.resize(image,(500,500))
#     blurimage = cv2.GaussianBlur(resizeimage,(5,5),-5)
#     grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(resizeimage,threshold1=100,threshold2=200)
#     os.chdir(path1)
#     cv2.imwrite(images[i],resizeimage)
#     os.chdir(path2)
#     cv2.imwrite(images[i],blurimage)
#     os.chdir(path3)
#     cv2.imwrite(images[i],grayimage)
#     os.chdir(path4)
#     cv2.imwrite(images[i],edges)
#     os.chdir("../")
#     cv2.imshow(images[i], grayimage)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()