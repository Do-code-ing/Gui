from tkinter import *
import tkinter.ttk as ttk

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

values = [str(i)+"일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=values) # height= 목록을 열었을 때 표시될 내용의 길이 values= 콤보박스내에 있는 값들 정의
combobox.set("카드 결제일") # 최초 목록 제목 설정 뿐 아니라 버튼 클릭을 통한 값 설정도 가능
combobox.pack()

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0) # 최초 값 지정 in 버튼 클릭을 통한 값
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게