from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        """
        Custom authentication logic to override the default JWT authentication.
        """
        print(request.headers)
        header = self.get_header(request)
        print("header :", header)

        if header is None:
            return None

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        print("access_token :", validated_token)

        # Optional: Here you can add additional checks or logic
        if not validated_token:
            raise AuthenticationFailed("Invalid token")

        return self.get_user(validated_token), validated_token
