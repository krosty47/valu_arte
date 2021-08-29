import unittest

from test_setup import test 
from tests.data.login_constants import LoginConstants
from exceptions.exception_non_existent_user import NonExistentUser
from exceptions.exception_invalid_password import InvalidPassword

class TestServiceLogin(unittest.TestCase):

    login_constants = LoginConstants()


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

    def __then_throw_exception_non_existent_user(self):
        self.assertRaises(NonExistentUser, self.service_login.validate_user,
                          self.login_constants.NON_EXISTING_EMAIL,
                          self.login_constants.ANY_PASSWORD)
    
     def __then_throw_exception_invalid_password(self):
        self.assertRaises(InvalidPassword, self.service_login.validate_user,
                          self.login_constants.EXISTING_EMAIL, self.login_constants.PASSWORD_INVALID)