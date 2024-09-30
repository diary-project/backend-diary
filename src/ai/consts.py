class TextModels:
    class Types:
        GPT_4_O = "gpt-4o"
        GPT_4_O_MINI = "gpt-4o-mini"
        GPT_4_TURBO = "gpt-4-turbo"
        GPT_4 = "gpt-4"
        GPT_3_5_TURBO = "gpt-3.5-turbo"


class ImageModels:
    class Types:
        DALL_E_3 = "dall-e-3"

    class Qualities:
        STANDARD = "standard"
        HD = "hd"

    class Sizes:
        SIZE_256 = "256x256"
        SIZE_512 = "512x512"
        SIZE_1024 = "1024x1024"
        SIZE_1792 = "1792x1024"
        SIZE_1024_1792 = "1024x1792"


class TextPrompts:
    INITIALIZE_PROMPTS = [
        {
            "role": "user",
            "content": "너는 세계최고의 키워드 추출모델이야 나는 너에게 누군가의 일기를 줄거고 너는 여기서 가장 적합한 키워드를 3개 ~ 5개를 추출할거야 "
            "키워드는 무조건 한단어야 그럼 너는 아래 [일기] 의 내용을 기반으로 [결과] 의 포맷에 맞게 나에게 응답을 줘 "
            "지금 현재 내용의 응답은 네 라고만 대답하고 나는 그 다음부터 너에게 일기를 줄거야\n\n"
            "[결과]\n"
            "별도의 텍스트 없이 키워드 만 응답해주고 그 결과를 # 으로 구분해",
        },
        {"role": "system", "content": "네"},
    ]
    PROMPT = "[일기]\n%s"


class ImagePrompts:
    PROMPT = "아래 [일기]에 적힌 내용을 보고 일기의 상황에 맞는 그림을 그려줘 [일기] : %s"
