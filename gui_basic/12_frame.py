from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

Label(root, text="메뉴를 선택해 주세요.").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# 버거 프레임
frame_burger = Frame(root, relief="solid", bd=1) # relief="solid" = 테두리 모양, bd = 외곽선 두께
frame_burger.pack(side="left", fill="both", expand=True) # side= 위치, fill= 위 아래로 채우기, expand= 사방향으로 확대

Button(frame_burger, text="햄버거").pack() # Frame 만든 곳에 넣을 버튼이라 root대신 frame_burger 기입
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="음료") # 이름이 있는 프레임으로 만들기
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게