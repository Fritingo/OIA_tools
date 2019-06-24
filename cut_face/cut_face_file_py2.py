import tkinter as tk
import tkinter.filedialog
import tkinter, tkFileDialog
import cv2
#import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
 
root=tk.Tk()     #建立視窗容器物件
root.title("Tk GUI")


def a():
    filename1 = tkinter.filedialog.askopenfilename()
    t1.delete(1.0,tk.END)
    t1.insert(1.0,filename1)
def b():
    filename2 = tkFileDialog.asksaveasfilename()
    t2.delete(1.0,tk.END)
    t2.insert(1.0,filename2)

def detect(in_f,out_f):
    img = cv2.imread(in_f)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.2,
                                          minNeighbors=1,)

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
    img2=img[y_center-h_range:y_center+h_range,x_center-w_range:x_center+w_range]
    cv2.imwrite(out_f,img2)
    
def cut_face():
    in_f = t1.get(1.0,tk.END)[:-1]
    print(type(in_f))
    in_f = in_f.decode('utf-8')
    print(in_f)
    out_f = t2.get(1.0,tk.END)[:-1]
    out_f = out_f.decode('utf-8')
    print(out_f)
    detect(in_f,out_f)
    label4=tk.Label(root, text="完成")   #建立標籤物件
    label4.pack()       #將元件放入容器

    
label1=tk.Label(root, text="輸入圖片")   #建立標籤物件
label1.pack()       #將元件放入容器
button1=tk.Button(root, text="選擇位置",command=a)
button1.pack()     #將元件放入容器
t1 = tk.Text(root,height=2)
t1.pack()
label2=tk.Label(root, text="輸出圖片")   #建立標籤物件
label2.pack()       #將元件放入容器
button2=tk.Button(root, text="選擇位置及檔名",command=b)
button2.pack()     #將元件放入容器
t2 = tk.Text(root,height=2)
t2.pack()
label3=tk.Label(root, text="大頭貼轉換")   #建立標籤物件
label3.pack()       #將元件放入容器
button3=tk.Button(root, text="開始",command=cut_face)
button3.pack() 
root.mainloop()