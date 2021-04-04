from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode="extended", height=0) # 여러가지 값을 리스트 형식으로 관리하는 목록 위젯, extended = 여러가지 값을 한 번에 선택 가능
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(0) # 삭제

    # 갯 수 확인
    # print("리스트에는", listbox.size(),"개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    # print("첫 번째부터 세 번째까지의 항목 : ", listbox.get(0,2))

    # 선택된 항목 확인 (위치로 반환 ex)0,1,2,3)
    print("선택된 항목 :", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게