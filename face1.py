####################################################
# Modified by Nazmi Asri                           #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Import OpenCV2 for image processing
import cv2
import os
import serial
from time import sleep #M
#ser = serial.Serial('/dev/ttyACM0', 115200)
#print (ser.readline())

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Start capturing video 
vid_cam = cv2.VideoCapture(0)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, one face id
face_id = 1

# Initialize sample face image
count = 0

assure_path_exists("dataset/")

servoTiltPosition = 90
servoPanPosition = 90
#tiltChannel = 0
#panChannel = 1
midScreenY=120
midScreenX=160



# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
        
        midFaceY=y+(h/2);
        midFaceX=x+(w/2);
        if(midFaceY < (midScreenY - 10)):
         if(servoTiltPosition >= 5):
          servoTiltPosition -= 1
        elif(midFaceY > (midScreenY +10)):
         if(servoTiltPosition <= 175):
          servoTiltPosition +=1

        if(midFaceX < (midScreenX - 10)):
         if(servoPanPosition >= 5):
          servoPanPosition -= 1
        elif(midFaceX > (midScreenX + 10)):
         if(servoPanPosition <= 175):
          servoPanPosition +=1

        file = open("vio.txt","a") # M
        file.write("%d\r\n" % (0))# M pan
        sleep(.5)# M
        file.write("%d\r\n" % (servoTiltPosition))# M tilt
        sleep(.5)# M
        file.write("%d\r\n" % (1))# M pan
        sleep(.5)# M
        file.write("%d\r\n" % (servoPanPosition))  # M pan
        sleep(.5)# M
        #print (x,y)
        # Increment sample face image
        count += 1
        #ser.wrie (count)
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count>1000:
        break

# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
