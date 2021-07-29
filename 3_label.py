from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

label1 = Label(root, text="Hello")
label1.pack()

photo = PhotoImage(file="C:/Users/Dero/Desktop/GUI_programming/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="See Ya")

    global photo2 # 전역변수(불필요한 메모리 날리는 걸 방지)
    photo2 = PhotoImage(file="C:/Users/Dero/Desktop/GUI_programming/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()

root.mainloop()
