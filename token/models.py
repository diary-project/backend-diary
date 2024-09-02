class Jwt:
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token


class Token:
    def __init__(self, token):
        self.token = token


class AccessToken(Token):
    def __init__(self, token):
        super().__init__(token)


class RefreshToken(Token):
    def __init__(self, token):
        super().__init__(token)
