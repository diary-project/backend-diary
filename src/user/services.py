from user.models import User


def update_nickname(user: User, nickname: str) -> User:
    user.nickname = nickname
    user.save()
    return user
