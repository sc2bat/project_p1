from tkinter import *

root = Tk()
root.title("dodo GUI")
root.geometry("640x480")

# 여러 줄에 걸쳐서 리스트 항목 정리
listbox = Listbox(root, selectmode="extended", height=0)
# extended 하나 혹은 여러개 선태가능 single 하나만 선택가능
# height 값에 따라 보여지는 리스트 항목이 제한됨
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "melon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # listbox.delete(END) # 젤 뒤에 삭제
    # listbox.delete(0) # 맨 앞부터 삭제

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))

    # 선택된 항목 확인 (위치로 반환) 1,2,3,
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()
