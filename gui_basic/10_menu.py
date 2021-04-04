from tkinter import *

root = Tk() # Tk class 호출, 그 안의 함수 및 변수 사용
root.title("Nado GUI") # 타이틀 설정
root.geometry("640x480") # 프로그램 창 크기, 가로 * 세로, 등장 위치 좌표
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 구분 자
menu_file.add_command(label="Open File...")
menu.add_cascade(label="File", menu=menu_file) # 앞서 만든 것들을 cascade(계단식배열)로 더해준다. 
menu_file.add_separator()
menu_file.add_command(label="Save all", state="disable") # 비활성화 state= 상태
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) # 종료

# Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python") # 라디오 버튼으로 만들기
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap") # 체크 박스 버튼으로 만들기
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu) # 위에서 만든 메뉴가 화면에 등장할 수 있게 처리

root.mainloop() # 이벤트 루프 같은 역할, 창이 유지되고 돌아가게