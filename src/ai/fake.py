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
                    "content": ("#안녕 #세상 #키워드 #샘플"),
                },
                "finish_reason": "length",
            }
        ],
        "usage": {
            "prompt_tokens": 23,
            "completion_tokens": 150,
            "total_tokens": 173,
            "completion_tokens_details": {"reasoning_tokens": 0},
        },
        "system_fingerprint": "fp_3a215618e8",
        "service_tier": None,
    }

    return chat_completion_data


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
                "url": "https://picsum.photos/200",
            }
        ],
    }

    return images_response_data
