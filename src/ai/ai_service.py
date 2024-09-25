import openai

from typing import Literal, Optional
from ai.consts import TextModels, ImageModels
from ai.openai_client import get_openai_client


def generate_text(
    prompt: str,
    model: str = TextModels.Types.GPT_4_O_MINI,
    max_tokens: int = 150,
    response_count: int = 1,
    stop_condition: str | None = None,
    temperature: float = 0.7,
) -> str:
    """
    OpenAI GPT 모델을 사용하여 텍스트 생성

    Args:
        prompt: 사용자 입력 문장
        model: 사용할 모델
        max_tokens: 응답의 최대 토큰 수
        response_count: 응답의 개수
        stop_condition: 응답 중지 조건
        temperature: 텍스트의 다양성 조정

    Returns:
        generated_text: AI가 생성한 텍스트
    """
    try:
        client = get_openai_client()

        # OpenAI GPT 모델에 요청 보내기
        generate_text_response = client.chat.completions.create(
            model=model,  # 사용할 모델 선택
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens,  # 응답의 최대 토큰 수
            n=response_count,  # 응답의 개수
            stop=stop_condition,  # 응답 중지 조건
            temperature=temperature,  # 텍스트의 다양성 조정
        )
        generated_text = generate_text_response["choices"][0]["message"]["content"].strip()
        return generated_text
    except openai.OpenAIError as e:
        print(e.http_status)
        print(e.error)


def generate_image(
    prompt: str,
    model: str = ImageModels.Types.DALL_E_3,
    image_count: int = 1,
    image_quality: Literal["standard", "hd"] = ImageModels.Qualities.STANDARD,
    image_size: Optional[
        Literal["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"]
    ] = ImageModels.Sizes.SIZE_256,
) -> str:
    """
    OpenAI 모델을 사용하여 이미지 생성

    Args:
        prompt:
        model:
        image_count:
        image_quality:
        image_size:

    Returns:

    """
    try:
        client = get_openai_client()

        generate_image_response = client.images.generate(
            model=model,
            prompt=prompt,
            n=image_count,
            quality=image_quality,
            size=image_size,
        )

        image_url = generate_image_response.data[0].url
        return image_url
    except openai.OpenAIError as e:
        print(e.http_status)
        print(e.error)
