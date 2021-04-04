from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

txt = Text(root, width=30, height=5) # 글을 입력할 수 있는 텍스트 박스 생성, 텍스트 박스 크기 조절 가능
txt.pack()
txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30) # 글을 입력할 수 있는 한 줄의 텍스트 박스 생성
e.pack()
e.insert(END, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 = 첫 번째 라인, 0 = 0번째 column위치
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게