from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # 프로그램 창의 x(너비), y(높이) 값 변경 불가, 결과적으로 최대화 기능 상실

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게