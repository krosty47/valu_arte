import unittest
import json
from app import app
from controller.controller_login import *
from tests.test_setup import test
from exceptions.message import Message
from tests.data.login_constants import LoginConstants
from tests.fixtures.fixture_user import FixtureUser
from tests.fixtures.fixture_email_not_unique import FixtureEmailNotUnique
# from tests.fixtures.fixture_user_name_not_unique import FixtureUserNameNotUnique

class TestControllerLogin(unittest.TestCase):

# 404 NOT FOUND
# 500 
# always import the controller you want to test

    login_constants = LoginConstants()
    message = Message()

    @test.database
    def test_unsuccessful_login_due_to_non_existent_user(self):
        # given a non existent user
        response = self.__when_login(
            self.login_constants.NON_EXISTING_EMAIL, self.login_constants.ANY_PASSWORD)
        self.__then_return_exception_non_existent_user(response)
    
    @test.database
    def test_login_succesfull(self):
        self.__given_an_existent_user()
        response = self.__when_login(
            self.login_constants.EXISTING_EMAIL, self.login_constants.PASSWORD_VALID)
        self.__then_return_a_token(response)
    
    @test.database
    def test_unsuccessful_login_due_to_invalid_password(self):
        self.__given_an_existent_user()
        response = self.__when_login(
            self.login_constants.EXISTING_EMAIL, self.login_constants.PASSWORD_INVALID)
        self.__then_return_exception_invalid_password(response)
    
    @test.database
    def test_unsuccessful_login_due_to_more_than_one_user_with_the_same_email(self):
        self.__given_two_users_with_the_same_email()
        response = self.__when_login(
            self.login_constants.EXISTING_EMAIL, self.login_constants.PASSWORD_INVALID)
        self.__then_return_exception_email_not_unique(response)
    
    # @test.database
    # def test_unsuccessful_login_due_to_more_than_one_user_with_the_same_user_name(self):
    #     self.__given_two_users_with_the_same_user_name()
    #     response = self.__when_login(
    #         self.login_constants.EXISTING_EMAIL, self.login_constants.PASSWORD_VALID)
    #     self.__then_return_exception_user_name_not_unique(response)
    
    def __given_an_existent_user(self):
        FixtureUser.run()
    
    def __given_two_users_with_the_same_email(self):
        FixtureEmailNotUnique.run()
        
    # def __given_two_users_with_the_same_user_name(self):
    #     FixtureUserNameNotUnique.run()


    def __when_login(self, email, password):
        tester = app.test_client(self)
        json_data_login = {"email": email, "password": password}
        response = tester.post(
            '/api/v1/login', json=json_data_login, content_type='application/json')
        return response
    
    
    def __then_return_exception_non_existent_user(self, response):
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("message"),
                         self.message.USERNAME_DOES_NOT_EXIST)
                    
    def __then_return_a_token(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json.loads(response.data).get('token'))
    
    def __then_return_exception_invalid_password(self, response):
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json.get("message"),
                         self.message.THE_PASSWORD_IS_INVALID)
    
    def __then_return_exception_email_not_unique(self, response):
        self.assertEqual(response.status_code, 500)
        self.assertTrue(response.json.get("message").find(
                         self.message.MORE_THAN_ONE_USER_WITH_THE_SAME_EMAIL))
    
    # def __then_return_exception_user_name_not_unique(self, response):
    #     self.assertEqual(response.status_code, 500)
    #     self.assertTrue(response.json.get("message").find(
    #                      self.message.MORA_THAN_ONE_USER_WITH_THE_SAME_USER_NAME))

if __name__ == '__main__':
    unittest.main()