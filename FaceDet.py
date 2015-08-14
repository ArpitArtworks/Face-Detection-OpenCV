#This code is valid for Open CV 2.4.9 and Python 2.7.5 for 32 Bit. Configuration has to be made accordingly to run this. Additionally, the ffmpeg folder in OpenCV folder
#has to be added to System Path Environment with the dll files renamed to opencv_ffmpegXYZ.dll where XYZ is the version X.YZ. Here, XYZ is 249.


import cv2

cap=cv2.VideoCapture("C:/Users/Ashris/Desktop/Test.mp4")
face_cascade_name = ("C:/Users/Ashris/Desktop/haarcascade_frontalface_alt.xml")
pface_cascade_name=("C:/Users/Ashris/Desktop/lbpcascade_profileface.xml")

face_cascade=cv2.CascadeClassifier()
pface_cascade=cv2.CascadeClassifier()

face_cascade.load(face_cascade_name)
pface_cascade.load(pface_cascade_name)

fourcc=cv2.cv.CV_FOURCC(*'XVID')
out=cv2.VideoWriter('Nebraska.mp4',fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret,frame=cap.read()
    result_image=frame.copy()
    faces = face_cascade.detectMultiScale(frame, 1.1, 2, 0|cv2.cv.CV_HAAR_SCALE_IMAGE, (30, 30))

    if len(faces) != 0:         
        for f in faces:         

          
            x, y, w, h = [ v for v in f ]
            

            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,0), 5)

            
            sub_face = frame[y:y+h, x:x+w]
            # Blur this effin pic
            sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
  
            result_image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
            
            
    pfaces = pface_cascade.detectMultiScale(result_image, 1.1, 2, 0|cv2.cv.CV_HAAR_SCALE_IMAGE, (30, 30))

    if len(pfaces) != 0:         # Agar face mila to ye karo
        for f in pfaces:         # Har chehera

          
            x, y, w, h = [ v for v in f ]
            

            cv2.rectangle(result_image, (x,y), (x+w,y+h), (255,255,0), 5)

            
            sub_face = result_image[y:y+h, x:x+w]
 
            sub_face = cv2.GaussianBlur(sub_face,(23, 23), 30)
  
            result_image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face

            out.write(result_image)
    cv2.imshow('frame',result_image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
out.release()
cap.release()
cv2.destroyAllWindows()
