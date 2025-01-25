import tkinter as tk

'''
파일명: screen.py
위치: ch14/screens/
설명: GUI구현
'''

def open_program_menu():
    # 화면(창) 생성
    GEOMETRY = "500x600"

    # 기본 창 설정 (창 제목 / 창 사이즈)
    root = tk.Tk()
    root.geometry(GEOMETRY)
    root.title("프로그램 메뉴")

    root.mainloop()

if __name__ == "__main__":
    open_program_menu()













