import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image_path = 'yogi.png'
# resize = cv2.resize(image_path,(494,1062.3333))
image = cv2.imread(image_path)
print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 120, 255), 7)

# Display the result
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()