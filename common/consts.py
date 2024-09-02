class KakaoUrls:
    AUTHORIZE_URL = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id=%s&redirect_uri=%s"
    ACCESS_TOKEN_URL = "https://kauth.kakao.com/oauth/token"
    VALIDATE_TOKEN_URL = "https://kapi.kakao.com/v1/user/access_token_info"
    PROFILE_URL = "https://kapi.kakao.com/v2/user/me"


class CallBackUrls:
    CALLBACK_TOKEN_URL = "http://localhost:8000/accounts/kakao/login/callback/"
    CALLBACK_AUTH_URL = "http://localhost:8000/oauth/token/"
    REDIRECT_URL = "http://localhost:5173/oauth/kakao/callback/"


class KakaoCodes:
    CLIENT_SECRET = "6rsrS3pFA0malvUhQDEsHEzuOVSaiBAK"
    APP_KEY_REST_API = "d8b18f9c8400928f811d2707fa87b6aa"
    APP_KEY_JS = "2cedd03381d813e8d0954ce34463e711"
    APP_KEY_ADMIN = "47e64dace240a8f3df405c9016b7cee8"
