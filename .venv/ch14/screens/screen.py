import tkinter as tk

'''
파일명: screen.py
위치: ch14/screens/
설명: GUI구현
'''


def create_screen(title: str):
    # 화면(창) 생성
    GEOMETRY = "500x600"

    # 기본 창 설정 (창 제목 / 창 사이즈)
    root = tk.Tk()
    root.geometry(GEOMETRY)
    root.title(title)

    return root


def open_program_menu():
    root = create_screen("프로그램 메뉴")

    # 회원가입 버튼
    button_signup = tk.Button(root, text="회원가입", command=lambda: open_signup_window())

    # 로그인 버튼
    button_login = tk.Button(root, text="로그인", command=lambda: open_login_window())

    # 버튼 모양 지정 및 노출
    button_signup.pack(pady=20)
    button_login.pack(pady=20)

    root.mainloop()

    return True


def open_signup_window():
    from ch14.services.auth import sign_up
    root = create_screen("회원가입")

    # 아이디 입력
    label_id = tk.Label(root, text="아이디를 입력하세요")
    label_id.pack(pady=20)
    entry = tk.Entry(root)
    entry_id = entry
    entry_id.pack()

    # 비밀번호 입력
    label_password = tk.Label(root, text="비밀번호를 입력하세요")
    label_password.pack(pady=20)
    entry_password = tk.Entry(root)
    entry_password.pack()

    # 사용자 이름 입력
    label_name = tk.Label(root, text="이름을 입력하세요")
    label_name.pack(pady=20)
    entry_name = tk.Entry(root)
    entry_name.pack()

    # 이메일 입력
    label_email = tk.Label(root, text="이메일을 입력하세요")
    label_email.pack(pady=20)
    entry_email = tk.Entry(root)
    entry_email.pack()

    # 버튼 생성하기(가입/취소)
    frame = tk.Frame(root)
    frame.pack(pady=50)

    button_confirm = tk.Button(frame, text="가입",
                               command=lambda: sign_up(entry_id.get(),
                                                       entry_password.get(),
                                                       entry_name.get(),
                                                       entry_email.get()
                                                       )
                               )
    button_cancel = tk.Button(frame, text="취소", command=lambda: root.destroy())

    button_confirm.pack(side="left")
    button_cancel.pack(side="left")

    root.mainloop()


def open_login_window():
    from ch14.services.auth import sign_in
    root = create_screen("로그인")

    # 사용자 이름 입력
    label_id = tk.Label(root, text="아이디를 입력하세요")
    label_id.pack(pady=20)
    entry_id = tk.Entry(root)
    entry_id.pack()

    # 이메일 입력
    label_password = tk.Label(root, text="비밀번호를 입력하세요")
    label_password.pack(pady=20)
    entry_password = tk.Entry(root)
    entry_password.pack()

    # 버튼 생성하기(가입/취소)
    frame = tk.Frame(root)
    frame.pack(pady=50)

    button_confirm = tk.Button(frame,
                               text="확인",
                               command=lambda: sign_in(entry_id.get(), entry_password.get())
                               )
    button_cancel = tk.Button(frame, text="취소", command=lambda: root.destroy())

    button_confirm.pack(side="left")
    button_cancel.pack(side="left")

    root.mainloop()


def open_weather_window():
    from ch14.services.weather import get_geocoding_data
    root = create_screen("날씨 검색")

    label_search = tk.Label(root, text="지역명을 입력해주세요.")
    label_search.pack(pady=30)
    entry_search = tk.Entry(root)
    entry_search.pack(pady=30)

    button_search = tk.Button(root, text="검색", command=lambda: get_geocoding_data(entry_search.get()))
    button_search.pack(pady=15)

    button_close = tk.Button(root, text="닫기", command=lambda: root.destroy())
    button_close.pack(pady=15)

    root.mainloop()


def open_weather_result_window(temp: int, feels_like: int, humidity: int, pop: float):
    root = create_screen("날씨 정보")
    label_title = tk.Label(root, text="날씨 조회 결과")
    label_title.pack()

    tk.Label(root, text=f"온도: {temp}도").pack(pady=10)
    tk.Label(root, text=f"체감 온도: {feels_like}도").pack(pady=10)
    tk.Label(root, text=f"습도: {humidity}%").pack(pady=10)
    tk.Label(root, text=f"강수 확률: {pop}%").pack(pady=10)

    tk.Button(root, text="닫기", command=lambda: root.destroy()).pack(pady=10)

    root.mainloop()


def open_mypage_window():
    root = create_screen("마이페이지")

    button_lotto = tk.Button(root, text="로또 번호 발송하기", command=lambda: open_lotto_window()).pack(pady=10)
    button_weather = tk.Button(root, text="날씨 조회하기", command=lambda: open_weather_window()).pack(pady=10)
    button_close = tk.Button(root, text="닫기", command=lambda: root.destroy()).pack(pady=10)

    root.mainloop()


def open_lotto_window():
    from ch14.services.lotto import send_lotto
    root = create_screen("로또 번호 발송")
    button_send = tk.Button(root, text="로또 번호 이메일 발송", command=lambda: send_lotto()).pack(pady=10)
    button_close = tk.Button(root, text="닫기", command=lambda: root.destroy()).pack(pady=10)


if __name__ == "__main__":
    open_mypage_window()
