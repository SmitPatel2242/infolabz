import cv2,os

###################   DELETE IMAGES   ##############################
val=input("Enter y for erase all data : ")
if val=="y":
    l = ["blur", "gray", "resize", "edges"]
    if "image" not in os.listdir():
        print("directory not exist")
        exit()
    os.chdir("./image")
    if os.listdir():
        for i in l:
            for item in os.listdir(i):
                item_path = os.path.join(i, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
    for i in l:
        if i in os.listdir():
            os.rmdir(i)
    os.chdir("../")
    os.rmdir("image")
    print("data deleted successfully")
    exit()


###################   DELETE IMAGES   ##############################



image = ["1.webp","2.webp","3.jpeg","4.webp","5.jpeg","6.jpeg","7.webp","8.jpeg","9.jpeg","10.jpeg"]
type = ["blur","resize","edges","gray"]
if "image" not in os.listdir():
    os.mkdir("image")
os.chdir("./image")
for i in type:
    if i not in os.listdir():
        os.mkdir(i)
os.chdir("../images")
for i in image:
    read = cv2.imread(i)
    resizeimage = cv2.resize(read,(500,500))
    blurimage = cv2.GaussianBlur(resizeimage,(5,5),-5)
    grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(resizeimage,threshold1=100,threshold2=200)
    os.chdir("../image/blur")
    cv2.imwrite(i,blurimage)
    os.chdir("../edges")
    cv2.imwrite(i,edges)
    os.chdir("../gray")
    cv2.imwrite(i,grayimage)
    os.chdir("../resize")
    cv2.imwrite(i,resizeimage)
    os.chdir("../../images")

print("Image Stored Successfully")