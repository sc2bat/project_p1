# 그리드 격자

from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

btn1 = Button(root, text="btn1")
btn2 = Button(root, text="btn2")

# btn1.pack(side="left")
# btn2.pack(side="right")

btn1.grid(row=0, column=0)
btn2.grid(row=1, column=1)

root.mainloop()