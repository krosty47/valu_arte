import unittest
from app import app
from controller.controller_login import *
from tests.test_setup import test
from exceptions.message import Message
from tests.data.login_constants import LoginConstants

class TestControllerLogin(unittest.TestCase):

# 404 NOT FOUND
# always import the controller you want to test

    login_constants = LoginConstants()
    message = Message()

    @test.database
    def test_unsuccessful_login_due_to_non_existent_user(self):
        # given a non existent user
        response = self.__when_login(
            self.login_constants.NON_EXISTING_EMAIL, self.login_constants.ANY_PASSWORD)
        self.__then_return_exception_non_existent_user(response)
    
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