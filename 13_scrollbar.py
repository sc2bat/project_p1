# Scrollbar

from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand =scrollbar.set)
# set으로 스크롤바 컨트롤
for i in range(1, 32): # 1 ~31
    listbox.insert(END, str(i) + "day")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()