import unittest
from unittest.mock import MagicMock
from encryptors.md5 import MD5

from tests.test_setup import test
from service.service_user import ServiceUser
from service.service_login import ServiceLogin
from tests.fixtures.fixture_user import FixtureUser
from service.service_security import ServiceSecurity
from tests.data.login_constants import LoginConstants
from exceptions.exception_non_existent_user import NonExistentUser
from exceptions.exception_invalid_password import InvalidPassword

class TestServiceLogin(unittest.TestCase):

    login_constants = LoginConstants()
    service_user = ServiceUser()
    service_security = ServiceSecurity()
    encryptor = MD5()
    service_login = ServiceLogin(service_user, service_security, encryptor)


    @test.database
    def test_user_invalid_return_non_existent_user(self):
        # given a non existent user
        # when login
        self.__then_throw_exception_non_existent_user()

    @test.database
    def test_user_with_invalid_password_return_invalid_password(self):
        self.__given_an_existent_user()
        # when login
        self.__then_throw_exception_invalid_password()
    
    @test.database
    def test_user_valid_with_password_valid(self):
        self.__given_an_existent_user()
        token = self.__when_login(
            self.login_constants.EXISTING_EMAIL, self.login_constants.PASSWORD_VALID)
        decoded_token = self.__when_decode_token(token)
        self.__then_return_a(token, decoded_token)
    
    def __given_an_existent_user(self):
        FixtureUser.run()

    def __when_login(self, email, password):
    # if we pass an argument to MagicMock, that argument will be the only token done.
        self.service_security.generate_token = MagicMock(return_value=self.login_constants.TOKEN_EXPECTED1)
        return self.service_login.validate_user(email, password)
    
    def __when_decode_token(self, token):
        decoded_token = self.service_security.decode_token(token)
        return decoded_token

    def __then_throw_exception_non_existent_user(self):
        self.assertRaises(NonExistentUser, self.service_login.validate_user,
                          self.login_constants.NON_EXISTING_EMAIL,
                          self.login_constants.ANY_PASSWORD)
    
    def __then_throw_exception_invalid_password(self):
        self.assertRaises(InvalidPassword, self.service_login.validate_user,
                          self.login_constants.EXISTING_EMAIL, self.login_constants.PASSWORD_INVALID)
    
    def __then_return_a(self, token, decoded_token: dict):
        self.assertEqual(self.login_constants.TOKEN_EXPECTED1, token)
        self.assertIsNotNone(decoded_token)
        self.assertIsNotNone(decoded_token.get('email'))
    

if __name__ == '__main__':
    unittest.main()