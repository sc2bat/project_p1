# 사지선다

from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

Label(root, text="pick your menu").pack()

# 하나의 목록으로 묶기
burger_var = IntVar() 
btn_burger1 = Radiobutton(root, text="Hamburger", value = 1, variable = burger_var)
btn_burger1.select() # 미리 선택
btn_burger2 = Radiobutton(root, text="Cheezeburger", value = 2, variable = burger_var)
btn_burger3 = Radiobutton(root, text="Chickenburger", value = 3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="pick your drink").pack()
# 음료 추가
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="Coke", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="Fanta", value="Fanta", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 선택된 라디오 항목의 value 출력
    print(drink_var.get()) # 음료 출력

btn = Button(root, text="order", command=btncmd)
btn.pack()

root.mainloop()
