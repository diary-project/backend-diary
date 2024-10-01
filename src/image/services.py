from diary.models import Diary
from ai.ai_service import OpenAIService, AIService
from image.consts import MAX_GENERATE_COUNT
from image.models import Image


def create_image(image_url: str, diary: Diary, prompt: str) -> Image:
    """
    Image를 생성합니다.
    """
    try:
        return Image.objects.create(prompt=prompt, url=image_url, diary=diary)
    except Exception as e:
        print(e)
        return None


def generate_image(diary: Diary, ai_service: AIService):
    """
    Diary에 이미지를 생성합니다.
    """
    generated_image_url = ""
    generate_count = 0

    while generate_count < MAX_GENERATE_COUNT:
        try:
            generated_image_url = ai_service.generate_image(prompt=diary.content)
            break
        except Exception as e:
            print(e)
            generate_count += 1
            continue

    if (generate_count == MAX_GENERATE_COUNT) or (not generated_image_url):
        return None

    created_image = create_image(image_url=generated_image_url, diary=diary, prompt=diary.content)
    return created_image
