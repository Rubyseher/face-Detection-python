import cv2
from random import randrange 
trained_face_data =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam= cv2.VideoCapture(0)
while True:
        successfull_frame_read,frame=webcam.read()

        # img= cv2.imread('people.jpg')
        greyscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face_coordinates=trained_face_data.detectMultiScale(greyscaled_img)

        for x,y,w,h in face_coordinates:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),10)

        cv2.imshow("i am iron man",frame)

        key=cv2.waitKey(1)
        if key==81 or key==113:
            break
webcam.release()
# print(face_coordinates)

# # cv2.imshow("i am iron man",img)

# cv2.waitKey()
# print("hi")