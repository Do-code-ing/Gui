from tkinter import *
import os

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("제목 없음 - Windows 메모장") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표

frame = Frame(root)
frame.pack(fill="both", expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

in_text = StringVar()
text = Text(frame, yscrollcommand=scrollbar.set)
text.pack(fill="both", expand=True)
scrollbar.config(command=text.yview)

menu = Menu(root)

# 열기, 저장 파일 이름
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            text.delete("1.0", END)
            text.insert(END, file.read())

def save_file():
        with open(filename, "w", encoding="utf8") as file:
            file.write(text.get("1.0", END))

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="메뉴", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

root.config(menu=menu)

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게