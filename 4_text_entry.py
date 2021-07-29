from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")
# text 위젯
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "show me the money")

e = Entry(root, width=30)
e.pack()
e.insert(0, "qwerty")

def btncmd():
    print(txt.get("1.0", END)) # 1 은 첫번째줄부터 0 줄에서 젤 왼쪽
    print(e.get())
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END) # entry 는 0부터 가져왔으니까 0만 적기

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
