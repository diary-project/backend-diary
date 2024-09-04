from rest_framework_simplejwt.tokens import RefreshToken


class TokenUtil:
    @staticmethod
    def generate_token(user):
        refresh = RefreshToken.for_user(user)

        access_token = str(refresh.access_token)  # Access Token
        refresh_token = str(refresh)  # Refresh Token

        return {
            'access': access_token,
            'refresh': refresh_token,
        }
