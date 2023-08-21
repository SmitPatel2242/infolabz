import cv2

samplenum = 0
#load the pre-trained haar cascade classspacifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# open the webcame
cam = cv2.VideoCapture(0)
while True:
    #Read a frame from the camera
    ret, image = cam.read()
    #check if the frame was red successfully
    if not ret:
        print("Eroor: could not read frame from the camara.")
        break
    # Convert the frame to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(300,300))
    #Draw Rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 9)
        cv2.imwrite(f"image{samplenum}.jpg",image)
    ##Display the image with ectangles around the detected faces
    cv2.imshow("Frame",image)
    #Increment the sample number
    samplenum +=1
    #Break the loop if enough samples have been collected
    if samplenum > 20:
        break
    #check for key press and exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()