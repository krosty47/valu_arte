from encryptors.md5 import MD5
from exceptions.exception_invalid_password import InvalidPassword
from exceptions.exception_non_existent_user import NonExistentUser
from exceptions.message import Message

from service.service_security import ServiceSecurity
from service.service_user import ServiceUser
from constants.security_constants import SecurityConstants


class ServiceLogin():

    message = Message()

    service_user = None
    service_security = None
    encryptor = None

    def __init__(self, service_user=ServiceUser(), service_security=ServiceSecurity(), encryptor=MD5()):
        self.service_user = service_user
        self.service_security = service_security
        self.encryptor = encryptor

    def validate_user(self, email, password):
        user = self.service_user.get_user(email)
        self.__validate_password(user, password)
        return self.service_security.generate_token(email, SecurityConstants.ROL_ADMIN)

    def __validate_password(self, user, password):
        password_encrypted = self.encryptor.encrypt(password)
        if user.password != password_encrypted:
            raise InvalidPassword(self.message.THE_PASSWORD_IS_INVALID)

