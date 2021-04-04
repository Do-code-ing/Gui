from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

chkvar = IntVar() # chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar) # variable = 체크박스에 체크, 혹은 미체크 행위 시 그 값을 변수에 저장
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="1주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 = 체크 해제, 1 = 체크
    print(chkvar2.get())
    
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게