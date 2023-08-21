import cv2
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    #
    # # Display the resulting frame
    a=cv2.imshow('frame', frame)
    # 0
    # # the 'q' button is set as the
    # # quitting button you may use any
    # # desired button of your choice
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    #
    # # After the loop release the cap object
    #
    # # Destroy all the windows
    # cv2.destroyAllWindows()
    image = a
    resizeimage = cv2.resize(image,(100,200))
    blurimage = cv2.GaussianBlur(resizeimage,(5,5),-5)
    grayimage = cv2.cvtColor(resizeimage,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(resizeimage,threshold1=150,threshold2=300)
    # cv2.imshow("Image",resizeimage)
    # cv2.imshow("ImageB",blurimage)
    # cv2.imshow("ImageG",grayimage)
    cv2.imshow("ImageE",edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    vid.release()