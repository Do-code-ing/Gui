from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

frame= Frame(root) # 프레임 만들고
frame.pack()

scrollbar = Scrollbar(frame) # 프레임 안에 스크롤 바 생성
scrollbar.pack(side="right", fill="y") # 스크롤 바의 위치와 모양

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set) # scrollbar.set을 해줌으로 스크롤 바가 있어야 할 위치에 잘 있게 해줌.

for i in range(1,32): # 1 ~ 31일
    listbox.insert(END, str(i)+"일")

listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # 스크롤 바와 리스트 박스의 yview와 호환되게 함

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게