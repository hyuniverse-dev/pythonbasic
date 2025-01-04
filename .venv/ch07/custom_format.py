'''
파일명: custom_format.py
위치: .venv/ch07/
'''


def custom_print(message):
    message_length = len(message) * 2
    line = message_length * '*'
    print(
        f'''
    {line}
    {message}
    {line}
    '''
    )
