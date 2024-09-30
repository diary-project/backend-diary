import openai
from abc import ABC, abstractmethod
from typing import Literal, Optional, Any, Dict

from openai.types import ImagesResponse
from openai.types.chat import ChatCompletion

from ai.consts import TextModels, ImageModels, TextPrompts, ImagePrompts
from ai.openai_client import get_openai_client

# 개발에만 활용되는 임시용 함수
from ai.fake import get_mock_text_response, get_mock_image_response


# class AIService(ABC):
#     @abstractmethod
#     def generate_text(self, prompt: str, **kwargs):
#         """
#         OpenAI GPT 모델을 사용하여 텍스트 생성
#         """
#         NotImplementedError("generate_text 메서드를 구현해주세요.")
#
#     @abstractmethod
#     def __extract_content_from_text_reseponse(self, text_response: Any):
#         """
#         OpenAI ChatCompletion으로부터 content를 추출합니다.
#         """
#         NotImplementedError("__extract_content_from_text_reseponse 메서드를 구현해주세요.")
#
#     @abstractmethod
#     def generate_image(self, prompt: str, **kwargs):
#         """
#         OpenAI 모델을 사용하여 이미지 생성
#         """
#         NotImplementedError("generate_image 메서드를 구현해주세요.")
#
#     @abstractmethod
#     def __extract_image_url_from_image_response(self, image_response: Any):
#         """
#         OpenAI ImagesResponse로부터 이미지 URL을 추출합니다.
#         """
#         NotImplementedError("__extract_image_url_from_image_response 메서드를 구현해주세요.")


# class OpenAIService(AIService):
class OpenAIService:
    def generate_text(
        self,
        prompt: str,
        model: str = TextModels.Types.GPT_4_O_MINI,
        max_tokens: int = 150,
        response_count: int = 1,
        stop_condition: str | None = None,
        temperature: float = 0.7,
    ) -> str:
        """
        OpenAI GPT 모델을 사용하여 텍스트 생성
        GPT MINI 모델 이미지 생성 => 1024x1024 / standard / 0.04 달러 per image

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

            messages = TextPrompts.INITIALIZE_PROMPTS
            messages.append({"role": "user", "content": TextPrompts.PROMPT % prompt})

            generate_text_response: ChatCompletion = client.chat.completions.create(
                model=model,  # 사용할 모델 선택
                messages=messages,  # 사용자 입력 문장
                max_tokens=max_tokens,  # 응답의 최대 토큰 수
                n=response_count,  # 응답의 개수
                stop=stop_condition,  # 응답 중지 조건
                temperature=temperature,  # 텍스트의 다양성 조정
            )

            generated_text = self.__extract_content_from_text_reseponse(generate_text_response)
            return generated_text

        except openai.OpenAIError as e:
            raise e

    def __extract_content_from_text_reseponse(self, text_response: ChatCompletion) -> str:
        return text_response.choices[0].message.content

    def generate_image(
        self,
        prompt: str,
        model: str = ImageModels.Types.DALL_E_3,
        image_count: int = 1,
        image_quality: Literal["standard", "hd"] = ImageModels.Qualities.STANDARD,
        image_size: Optional[
            Literal["256x256", "512x512", "1024x1024", "1792x1024", "1024x1792"]
        ] = ImageModels.Sizes.SIZE_1024,
    ) -> str:
        """
        OpenAI 모델을 사용하여 이미지 생성
        DALLE-3 모델 이미지 생성 => 1024x1024 / standard / 0.04 달러 per image

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
            full_prompt = ImagePrompts.PROMPT % prompt
            generate_image_response: ImagesResponse = client.images.generate(
                model=model,
                prompt=full_prompt,
                n=image_count,
                quality=image_quality,
                size=image_size,
            )

            # GPT로 생성된 이미지는 1시간후 만료됨
            image_url = self.__extract_image_url_from_image_response(generate_image_response)
            return image_url

        except openai.OpenAIError as e:
            raise e

    def __extract_image_url_from_image_response(self, image_response: ImagesResponse) -> str:
        return image_response.data[0].url


# class FakeAIService(AIService):
#     def generate_text(self, prompt: str, **kwargs):
#         return self.__extract_content_from_text_reseponse(get_mock_text_response())
#
#     def __extract_content_from_text_reseponse(self, text_response: Dict):
#         return text_response["choices"][0]["message"]["content"]
#
#     def generate_image(self, prompt: str, **kwargs):
#         return self.__extract_image_url_from_image_response(get_mock_image_response())
#
#     def __extract_image_url_from_image_response(self, image_response: Dict):
#         return image_response["data"][0]["url"]
