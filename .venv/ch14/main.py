from ch14.screens.screen import open_program_menu

'''
파일명: main.py
위치: .venv/ch14/
'''

### 웰컴투파이썬 실행파일

if __name__ == "__main__":
    while True:
        response = open_program_menu()
        if response:
            break