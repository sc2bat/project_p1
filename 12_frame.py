# Frame

from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

Label(root, text="Select Menu").pack(side="top")

Button(root, text="order").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="CheezeHamburger").pack()
Button(frame_burger, text="ChickenHamburger").pack()

frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Fanta").pack()

root.mainloop()