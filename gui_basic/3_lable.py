import os
import sys
from tkinter import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표

lable1 = Label(root, text="안녕하세요")
lable1.pack()

photo = PhotoImage(file=resource_path("gui_basic/img.png"))
lable2 = Label(root, image=photo)
lable2.pack()

def change():
    lable1.config(text="또 만나요") # config = 변경. ~의 형태, 모양을 만들다 즉, lable1의 text내용을 변경
    global photo2
    photo2 = PhotoImage(file=resource_path("gui_basic/img2.png"))
    lable2.config(image=photo2)

btn = Button(root, text="클릭", command=change)

btn.pack()

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게