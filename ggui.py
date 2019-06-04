import tkinter as tk
import tkinter.filedialog
root=tk.Tk()     #建立視窗容器物件
root.title("Tk GUI")


def a():
    filename1 = tkinter.filedialog.askdirectory()
    t1.delete(1.0,tk.END)
    t1.insert(1.0,filename1)
    
def b():
    filename2 = tkinter.filedialog.askdirectory()
    t2.delete(1.0,tk.END)
    t2.insert(1.0,filename2)
    end_path = t2.get(1.0,tk.END)
    print(end_path)


    
label1=tk.Label(root, text="輸入資料夾")   #建立標籤物件
label1.pack()       #將元件放入容器
button1=tk.Button(root, text="選擇位置",command=a)
button1.pack()     #將元件放入容器
t1 = tk.Text(root,height=2)
t1.pack()
label2=tk.Label(root, text="輸出資料夾")   #建立標籤物件
label2.pack()       #將元件放入容器
button2=tk.Button(root, text="選擇位置",command=b)
button2.pack()     #將元件放入容器
t2 = tk.Text(root,height=2)
t2.pack()
label3=tk.Label(root, text="大頭貼轉換")   #建立標籤物件
label3.pack()       #將元件放入容器
button3=tk.Button(root, text="開始",command=b)
button3.pack() 
root.mainloop()