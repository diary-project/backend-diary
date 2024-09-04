import random


class UserUtil:
    @staticmethod
    def generate_random_kor_nickname(length=8):
        # 유니코드 한글 범위 (가 ~ 힣)
        CHO = list("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ")
        JUNG = list("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ")
        JONG = list("ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ")

        result = []
        for _ in range(length):
            cho = random.choice(CHO)
            jung = random.choice(JUNG)
            jong = random.choice(JONG + [''])  # 종성은 없어도 됨
            char = chr(0xAC00 + (CHO.index(cho) * 21 * 28) + (JUNG.index(jung) * 28) + JONG.index(jong))
            result.append(char)

        return ''.join(result)
