import json


def get_mock_text_response():
    chat_completion_data = {
        "id": "chatcmpl-ABb8igO1g4IsAPKhFtJb5XBhRDbtg",
        "object": "chat.completion",
        "created": 17227736,
        "model": "gpt-4o-mini-2024-07-18",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": (
                        "인공지능(Artificial Intelligence, AI)이란 컴퓨터가 인간의 지능을 모방하거나 "
                        "인간처럼 학습하고 문제를 해결하는 능력을 갖추도록 하는 기술 및 연구 분야를 말합니다. "
                        "인공지능은 다양한 영역에서 활용되며, 크게 두 가지 유형으로 나눌 수 있습니다.\n\n"
                        "1. *예를 들어, 음성 인식, 이미지 인식, 자연어 처리, 추천 시스템 등이 포함됩니다.\n\n"
                        "2. **강한 인공지능(Strong AI)**: 인간"
                    )
                },
                "finish_reason": "length"
            }
        ],
        "usage": {
            "prompt_tokens": 23,
            "completion_tokens": 150,
            "total_tokens": 173,
            "completion_tokens_details": {
                "reasoning_tokens": 0
            }
        },
        "system_fingerprint": "fp_3a215618e8",
        "service_tier": None
    }

    return json.dumps(chat_completion_data, indent=4, ensure_ascii=False)


def get_mock_image_response():
    images_response_data = {
        "created": 1727328181,
        "data": [
            {
                "b64_json": None,
                "revised_prompt": (
                    "An image of a bird perched on a tree. The bird is intricately detailed with vibrant "
                    "colors and intricate feather patterns. The tree is tall and majestic, its branches reaching "
                    "out in all directions, providing the bird with a natural perch. The background is filled "
                    "with a clear sky, and the sun is just peaking behind the tree, casting long shadows and "
                    "highlighting the scene with a warm, radiant glow."
                ),
                "url": (
                    "https://oaidalleapiprodscus.blob.core.windows.net/private/org-QvBdllEksCweukXk4LoxYok0/"
                    "user-B375KfMFZ12kpfcSK4CRZ6U7/img-grurOl7bp9IsUojfxZ4HeaWx.png?"
                    "st=2024-09-26T04%3A23%3A01Z&se=2024-09-26T06%3A23%3A01Z&sp=r&sv=2024-08-04&sr=b&"
                    "rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&"
                    "sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-09-25T23%3A22%3A11Z&"
                    "ske=2024-09-26T23%3A22%3A11Z&sks=b&skv=2024-08-04&sig=3GZQuhg/Aii8kyvpBz0RWPgEKTHYg68h2S4p59lN%2BHk%3D"
                )
            }
        ]
    }

    return json.dumps(images_response_data, indent=4)
