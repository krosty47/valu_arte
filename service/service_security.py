from exceptions.exception_authorization_error import AuthorizationError
from helper import Helper

from datetime import datetime, timedelta

import jwt


class ServiceSecurity():

    jwt_encoder_decoder = None
    config = Helper.loadEnv()

    def __init__(self, jwt_encoder_decoder=jwt):
        self.jwt_encoder_decoder = jwt_encoder_decoder

    def validate_authorization(self, authorization_header_data):
        if authorization_header_data is not None:
            token = str(authorization_header_data.replace("Bearer ", ""))
            try:
                return self.decode_token(token)
            except Exception:
                raise AuthorizationError("Invalid token")

        raise AuthorizationError("Not allowed")

    def generate_token(self, email):
        JWT_SECRET = self.config.get('JWT_SECRET')
        JWT_ALGORITHM = self.config.get('JWT_ALGORITHM')
        JWT_EXP_DELTA_SECONDS = int(self.config.get('JWT_EXP_DELTA_SECONDS'))
        payload = {
            'email': email,
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        token = self.jwt_encoder_decoder.encode(
            payload, JWT_SECRET, JWT_ALGORITHM)
        return token

    def decode_token(self, token: str) -> dict:
        verify_exp = False if self.config.get('ENVIRONMENT') == 'DEV' else True
        payload = self.jwt_encoder_decoder.decode(token, self.config.get(
            'JWT_SECRET'), algorithms=self.config.get('JWT_ALGORITHM'), options={"verify_exp": verify_exp})
        return payload
