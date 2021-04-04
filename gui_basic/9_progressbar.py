from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate = 가늠할 수 없는, 언제 끝날지 모르는 진행상황을 표시할 때 사용
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # determinate = 확실한, 명확한, <> indeterminate
# progressbar.start(10) # 프로그레스바가 시작되며, 10ms마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지

# btn = Button(root, text="선택", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # 실수 값을 포함하기 위해 정수+실수=double 뭐 이런 뜻인듯
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.05) # 0.01초 대기

        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # ui 업데이트
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게