# Messagebox 
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("title_m", "message")
def warn():
    msgbox.showwarning("title_w", "warning")
def error():
    msgbox.showerror("title_e", "error")
def okaycancel():
    msgbox.askokcancel("확인 / 취소", "확인 취소")
def reokaycancel():
    response = msgbox.askretrycancel("retry / 취소", "wanna retry?")
    print("response", response)
    if response == 1:
        print("재시도")
    elif response == 0:
        print("no")
def yesno():
    msgbox.askyesno("yes / no", "yes yes no no")
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="yes yes no no \n cancel cancel")
# yes : 저장 후 종료 # no : 저장 하지 않고 종료 # cancel : 프로그램 종료 취소
    print("response", response)
    if response == 1:
        print("yes")
    elif response == 0:
        print("no")
    else:
        print("cancel")


Button(root, command=info, text="alert").pack()
Button(root, command=warn, text="warning").pack()
Button(root, command=error, text="error").pack()

Button(root, command=okaycancel, text="okaycancel").pack()
Button(root, command=reokaycancel, text="retry").pack()
Button(root, command=yesno, text="yes no").pack()
Button(root, command=yesnocancel, text="yes no cancel").pack()


root.mainloop()