from typing import List

from diary.models import Diary
from tag.models import Tag
from ai.ai_service import generate_text


def create_tag(tag_name: str, diary: Diary) -> Tag:
    """
    Tag를 생성합니다.
    """

    # Tag 생성
    tag = Tag.objects.create(name=tag_name, diary=diary)
    return tag


def create_tags(tag_name_list: List[str], diary: Diary) -> List[Tag]:
    """
    여러개의 Tag를 생성합니다. 여러개의 Tag는 하나의 Diary에 속합니다.
    """

    # Tag 생성
    tag_list = [Tag(name=tag_name, diary=diary) for tag_name in tag_name_list]
    created_tag_list = Tag.objects.bulk_create(tag_list)
    return created_tag_list


def extract_tags_from_diary_content(diary: Diary):
    """
    Diary의 content로 부터 태그를 추출합니다.
    태그 추출은 LLM(Linear Learner Model)을 사용합니다.
    """

    # diary에서 content를 추출하여 인공지능의 Input으로 사용
    generated_content = generate_text(prompt=diary.content)

    # 생성된 Tag를 저장
    tag_name_list = extract_tags_from_generated_content(generated_content)
    created_tag_list = create_tags(tag_name_list)
    return created_tag_list


def extract_tags_from_generated_content(content: str) -> List[str]:
    """
    LLM 모델로 부터 생성된 content에서 태그를 추출합니다.
    """

    # TODO: 생성된 content를 추출하여 Tag 결과물을 추출

    # 생성된 Tag를 저장
    tag_list = []
    return tag_list
