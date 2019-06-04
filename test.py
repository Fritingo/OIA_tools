import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
 
def detect(filename,input_dir,output_dir):
    img = cv2.imread(input_dir+filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=1,)
    
#    print (faces)

    for (x,y,w,h) in faces:
#        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        x=x
        y=y
        w=w
        h=h
    x_center = int(x+(w/2))
    y_center = int((y+(h/2))*0.9)
    w_range = int((w/2)*1.4)
    h_range = int((h/2)*1.6)
    
    
#    img = cv2.rectangle(img,(x_center-w_range,y_center-h_range),(x_center+w_range,y_center+h_range),(0,255,0),2)
    
        
#    cv2.imwrite('./test_face.jpg', img)
    img2=img[y_center-h_range:y_center+h_range,x_center-w_range:x_center+w_range]
    #print(x_center,y_center,w_range,h_range)
    
    cv2.imwrite(output_dir+filename,img2)
 
if __name__ == "__main__":
    
    path = 'D:\oia_tool\input'
    for file in os.listdir(path):
        print(file)
    detect('images.jpg','./input/','./output/')