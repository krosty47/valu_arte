from exceptions.message import Message
from repository.repository_user import *

class ServiceUser():

    message = Message()

    repository_user = RepositoryUser()

    def get_user(self, email):
        users = self.repository_user.find_users_by_email(email)
        return self.validate_user(users)