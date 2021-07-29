# 진행상태 표시
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# # 맥시멈, 모드 
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="stop", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01 초 대기
        
        p_var2.set(i)
        progressbar2.update() # 매번 gui 업뎃
        print(p_var2.get())


btn = Button(root, text="start", command=btncmd2)
btn.pack()

root.mainloop()
