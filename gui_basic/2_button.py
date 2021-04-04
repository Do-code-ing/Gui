from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정

btn1 = Button(root, text="버튼1") # 넣을 위치, 버튼에 명시될 텍스트, 텍스트 값이 표시될 수 있게만 크기 결정
btn1.pack() # root창에 pack함수를 호출해 메인 윈도우에 포함

btn2 = Button(root, padx=5, pady=10, text="버튼2") # 넣을 위치, padx, pady = 텍스트가 명시된 뒤 + 좌우여백, + 상하여백, 텍스트
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # width, height 버튼의 크기 자체를 설정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg = 폰트색깔, bg = 배경색깔
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png") # 이미지 불러오기
btn6 = Button(root, image=photo) # imaage = 이미지 가져오기
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요.")
btn7 = Button(root, text="동작하는 버튼", command=btncmd) # command = 명령 입력
btn7.pack()


root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게