from ch14.utils import lotto_generator, mail

'''
파일명: lotto.py
위치: ch14/services/
'''


def send_lotto():
    # 로또 번호 생성
    numbers = lotto_generator.store_lotto()

    # 이메일 발송
    body = f"""
    첫 번째 번호: {numbers[0]}
    두 번째 번호: {numbers[1]}
    세 번째 번호: {numbers[2]}
    네 번째 번호: {numbers[3]}
    다섯 번째 번호: {numbers[4]}
    보너스 번호: {numbers[5]}
    
    당첨을 축하드립니다~ 짝짝짝~
    """

    members_email = ["abc1@email.com", "abc2@email.com", "abc3@email.com"]

    for email in members_email:
        mail.send_mail(
            email,
            "여보게~ 이번주 당첨번호라네~",
            body
        )
