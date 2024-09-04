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
    # kakao_auth_url = KakaoUrls.AUTHORIZE_URL % (KakaoCodes.APP_KEY_REST_API, CallBackUrls.CALLBACK_AUTH_URL)

    return HttpResponseRedirect(kakao_auth_url)


@api_view(["GET"])
def kakao_login(request):
    code = request.GET.get("code")
    user_profile = get_user_profile_from_kakao(code)
    user, _ = create_member(user_profile)

    # Token 생성하는 로직
    user_jwt = TokenUtil.generate_token(user)
    print(user_jwt)

    return Response(
        data=user_jwt,
        status=status.HTTP_200_OK
    )


def get_user_profile_from_kakao(code):
    access_token = request_kakao_access_token(code)
    validate_kakao_access_token(access_token)
    user_profile_response = request_kakao_user_info(access_token)
    return user_profile_response


def request_kakao_access_token(code):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    }

    data = {
        'grant_type': "authorization_code",
        'client_id': KakaoCodes.APP_KEY_REST_API,
        'redirect_uri': CallBackUrls.REDIRECT_URL,
        'client_secret': KakaoCodes.CLIENT_SECRET,
        'code': code
    }

    token_response = requests.post(
        KakaoUrls.ACCESS_TOKEN_URL,
        headers=headers,
        data=data,
    )

    token_json = token_response.json()
    return token_json.get('access_token')


def validate_kakao_access_token(access_token):
    headers = {
        "Authorization": f'Bearer {access_token}',
        'client_secret': KakaoCodes.CLIENT_SECRET,
    }

    token_validate_response = requests.get(
        KakaoUrls.VALIDATE_TOKEN_URL,
        headers=headers)

    token_validate_json = token_validate_response.json()
    # 별도 로직 처리


def request_kakao_user_info(access_token):
    headers = {
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        "Authorization": f'Bearer {access_token}'
    }
    user_info_response = requests.post(
        KakaoUrls.PROFILE_URL,
        headers=headers)

    user_info_json = user_info_response.json()
    return user_info_json


def create_member(user_profile):
    kakao_oid = user_profile.get("id")
    kakao_account = user_profile.get("kakao_account")
    email = kakao_account.get("email")
    nickname = UserUtil.generate_random_kor_nickname()

    return User.objects.get_or_create(
        email=email,
        defaults={
            "nickname": nickname,
            "kakao_oid": kakao_oid,
        },
    )
