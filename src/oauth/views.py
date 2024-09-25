from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.consts import KakaoUrls, KakaoCodes, CallBackUrls
from utils.user_utils import UserUtil
from utils.token_utils import TokenUtil
from utils.log_utils import Logger
from user.models import User

import requests


class KakaoRedirectView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        kakao_auth_url = KakaoUrls.AUTHORIZE_URL % (
            KakaoCodes.APP_KEY_REST_API,
            CallBackUrls.REDIRECT_URL,
        )
        Logger.debug(f"return url : {kakao_auth_url}")

        return HttpResponseRedirect(kakao_auth_url)


class KakaoLoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """
        카카오 로그인 후 콜백 URL로 code를 받아서 처리하는 로직

        1. code를 받아서 카카오에게 access token을 요청
        2. access token을 받아서 유효성 검사
        3. access token을 이용해서 사용자 정보 요청
        4. 사용자 정보로 유저 생성
        5. Token 생성 및 반환
        """
        code = request.GET.get("code")
        user_profile = get_user_profile_from_kakao(code)
        Logger.debug(f"user profile : {user_profile}")

        email, kakao_oid, nickname = get_user_info_by_profile(user_profile)
        Logger.info(f"email : {email} | nickname : {nickname}")
        Logger.debug(f"kakao_oid : {kakao_oid}")

        user, _ = get_or_create_member(email, kakao_oid, nickname)
        Logger.debug(f"user created -> id : {user.id}")

        # Token 생성하는 로직
        user_jwt = TokenUtil.generate_token(user)
        Logger.debug(
            f"token generated \naccess : {user_jwt.get("access")} \nrefresh : {user_jwt.get("refresh")}"
        )

        return Response(data=user_jwt, status=status.HTTP_200_OK)


def get_user_info_by_profile(user_profile):
    """
    카카오 프로필 정보를 받아서 유저 정보를 추출하는 로직

    :param user_profile: 카카오 프로필 정보
    :return: email, kakao_oid, nickname
    """
    kakao_oid = user_profile.get("id")
    kakao_account = user_profile.get("kakao_account")

    if not kakao_account:
        raise AttributeError("Kakao account can not be None")

    email = kakao_account.get("email")
    nickname = UserUtil.generate_random_kor_nickname()
    return email, kakao_oid, nickname


def get_user_profile_from_kakao(code):
    """
    카카오에게 code를 이용해서 사용자 정보를 요청하는 로직

    :param code: 카카오에서 받은 code
    :return: 사용자 정보
    """
    access_token = request_kakao_access_token(code)
    Logger.debug(f"kakao access token : {access_token}")

    validate_kakao_access_token(access_token)

    user_profile_response = request_kakao_user_info(access_token)

    return user_profile_response


def request_kakao_access_token(code):
    """
    카카오에게 code를 이용해서 access token을 요청하는 로직

    :param code: 카카오에서 받은 code
    :return: access token
    """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }

    data = {
        "grant_type": "authorization_code",
        "client_id": KakaoCodes.APP_KEY_REST_API,
        "redirect_uri": CallBackUrls.REDIRECT_URL,
        "client_secret": KakaoCodes.CLIENT_SECRET,
        "code": code,
    }

    token_response = requests.post(
        KakaoUrls.ACCESS_TOKEN_URL,
        headers=headers,
        data=data,
    )

    token_json = token_response.json()
    return token_json.get("access_token")


def validate_kakao_access_token(access_token):
    """
    카카오에게 access token을 이용해서 유효성 검사하는 로직

    :param access_token: 카카오에서 받은 access token
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "client_secret": KakaoCodes.CLIENT_SECRET,
    }

    token_validate_response = requests.get(
        KakaoUrls.VALIDATE_TOKEN_URL, headers=headers
    )

    token_validate_json = token_validate_response.json()
    # 별도 로직 처리


def request_kakao_user_info(access_token):
    """
    카카오에게 access token을 이용해서 사용자 정보를 요청하는 로직

    :param access_token: 카카오에서 받은 access token
    :return: 사용자 정보
    """
    headers = {
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        "Authorization": f"Bearer {access_token}",
    }
    user_info_response = requests.post(KakaoUrls.PROFILE_URL, headers=headers)

    user_info_json = user_info_response.json()
    return user_info_json


def get_or_create_member(email, kakao_oid, nickname):
    return User.objects.get_or_create(
        email=email,
        defaults={
            "nickname": nickname,
            "kakao_oid": kakao_oid,
        },
    )
