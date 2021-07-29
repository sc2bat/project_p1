# 진행상태 표시

import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# 맥시멈, 모드 
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # 작동 중지

btn = Button(root, text="stop", command=btncmd)
btn.pack()

root.mainloop()
