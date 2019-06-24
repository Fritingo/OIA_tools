import cv2
import os
import numpy as np
import sys  
from PIL import Image
#reload(sys)  
#sys.setdefaultencoding('gbk')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
 



def detect(filename,input_dir,output_dir):
    temp = Image.open(input_dir+filename)
    temp.save('temp.jpg','jpeg')
    img = cv2.imread('./temp.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=1,)
    
#    print (faces)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        x=x
        y=y
        w=w
        h=h
    x_center = int(x+(w/2))
    y_center = int((y+(h/2))*0.9)
    w_range = int((w/2)*1.4)
    h_range = int((h/2)*1.6)
    
    
    img = cv2.rectangle(img,(x_center-w_range,y_center-h_range),(x_center+w_range,y_center+h_range),(0,255,0),2)
    
        
    cv2.imwrite('./test_face.jpg', img)
    img2=img[y_center-h_range:y_center+h_range,x_center-w_range:x_center+w_range]
    
    #print(x_center,y_center,w_range,h_range)
    
    cv2.imwrite('temp.jpg',img2)
    save2org_name = Image.open('./temp.jpg')
    save2org_name.save(output_dir+filename,'jpeg')
 
if __name__ == "__main__":
#    a ='.\input\下載.jpg'
#    print(a)
#    a = a.decode('big5')
#    print(a)
#    a = a.encode('utf-8')
#    print(a)
#    shutil.copyfile('.\input\下載.jpg','ddd.jpg')
#    path = 'D:\oia_tool\input'
#    for file in os.listdir(path):
#        print(file)
    detect("下載.jpg",'./input/','./output/')