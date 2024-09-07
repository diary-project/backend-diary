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
            jong = random.choice(JONG + [""])  # 종성은 없어도 됨
            jong_index = 0 if jong == "" else JONG.index(jong)  # 종성이 없을 때는 0
            char = chr(
                0xAC00
                + (CHO.index(cho) * 21 * 28)
                + (JUNG.index(jung) * 28)
                + jong_index
            )
            result.append(char)

        return "".join(result)
