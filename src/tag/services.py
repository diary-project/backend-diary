from typing import List

from diary.models import Diary

from tag.models import Tag
from tag.const import MAX_GENERATE_COUNT

from ai.ai_service import AIService


def create_tag(tag_name: str, diary: Diary) -> Tag:
    """
    Tag를 생성합니다.
    """
    return Tag.objects.create(name=tag_name, diary=diary)


def create_tags(tag_list: List[Tag]) -> List[Tag]:
    """
    여러개의 Tag를 생성합니다. 여러개의 Tag는 하나의 Diary에 속합니다.
    """
    return Tag.objects.bulk_create(tag_list)


def extract_tags_from_diary_content(diary: Diary, ai_service: AIService):
    """
    Diary의 content로 부터 태그를 추출합니다.
    태그 추출은 LLM(Linear Learner Model)을 사용합니다.
    """

    generate_count = 0
    tag_list = []

    while generate_count < MAX_GENERATE_COUNT:
        try:
            generated_content = ai_service.generate_text(prompt=diary.content)
            tag_list.extend(build_tags_from_generated_content(generated_content, diary))
            break
        except ValueError as e:
            print(e)
            generate_count += 1
            continue

    if generate_count == MAX_GENERATE_COUNT:
        return tag_list

    # Tag 생성
    created_tag_list = create_tags(tag_list)
    return created_tag_list


def build_tags_from_generated_content(content: str, diary: Diary) -> List[Tag]:
    """
    LLM 모델로 부터 생성된 content에서 태그를 추출합니다.
    """
    tags = content.strip().split("#")

    processed_tags = []
    for tag in tags:
        cleaned_tag = tag.strip()

        if not cleaned_tag:
            continue
        if len(cleaned_tag) > 10:
            raise ValueError("태그의 길이가 10자를 초과했습니다.")

        processed_tag = Tag.build(word=cleaned_tag, diary=diary)
        processed_tags.append(processed_tag)

    if len(processed_tags) < 3:
        raise ValueError("태그의 개수가 3개 미만입니다.")

    return processed_tags
