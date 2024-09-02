from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.consts import KakaoUrls, KakaoCodes, CallBackUrls
from utils.user_utils import UserUtil
from utils.token_utils import TokenUtil
from user.models import User

import requests


@api_view(["GET"])
def kakao_redirect(request):
    kakao_auth_url = KakaoUrls.AUTHORIZE_URL % (KakaoCodes.APP_KEY_REST_API, CallBackUrls.REDIRECT_URL)

    return HttpResponseRedirect(kakao_auth_url)


@api_view(["GET"])
def kakao_login(request):
    code = request.GET.get("code")
    user_profile_response = kakao_process(code)

    user_profile = user_profile_response.json()
    created, user = create_member(user_profile)

    # Token 생성하는 로직
    user_jwt = TokenUtil.generate_token(user)
    return Response(
        data=user_jwt,
        status=status.HTTP_200_OK
    )


def kakao_process(code):
    access_token = request_kakao_access_token(code)
    validate_kakao_access_token(access_token)
    user_profile_response = request_kakao_user_info(access_token)
    return user_profile_response


def create_member(user_profile):
    kakao_oid = user_profile.get("id")
    email = user_profile.get("kakao_account")["email"]
    nickname = UserUtil.generate_random_kor_nickname()

    return User.objects.get_or_create(
        email=email,
        defaults={
            "nickname": nickname,
            "kakao_oid": kakao_oid,
        },
    )


def request_kakao_user_info(access_token):
    headers = {
        "Authorization": f'Bearer {access_token}',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
    }
    user_info_response = requests.post(
        KakaoUrls.PROFILE_URL,
        headers=headers)
    return user_info_response


def validate_kakao_access_token(access_token):
    headers = {
        "Authorization": f'Bearer {access_token}',
        'client_secret': KakaoCodes.CLIENT_SECRET,
    }

    token_validate_response = requests.get(
        KakaoUrls.VALIDATE_TOKEN_URL,
        headers=headers)


def request_kakao_access_token(code):
    # token 받아오기
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    }

    data = {
        'grant_type': "authorization_code",
        'client_id': KakaoCodes.APP_KEY_REST_API,
        'redirect_uri': CallBackUrls.CALLBACK_AUTH_URL,
        'client_secret': KakaoCodes.CLIENT_SECRET,
        'code': code
    }

    token_response = requests.post(
        KakaoUrls.ACCESS_TOKEN_URL,
        headers=headers,
        data=data,
    )
    return token_response.json().get('access_token')
