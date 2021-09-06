from exceptions.message import Message
from repository.repository_user import RepositoryUser
from exceptions.exception_non_existent_user import NonExistentUser
from exceptions.exception_user_email_not_unique import UserEmailNotUnique

class ServiceUser():

    message = Message()

    repository_user = RepositoryUser()

    def get_user(self, email):
        users = self.repository_user.find_users_by_email(email)
        return self.validate_user(users)
    
    def validate_user(self, users):
        self.validate_user_exist(len(users))
        self.validate_email_not_unique(len(users))
        return users[0]

    def validate_user_exist(self, len_users):
        if len_users == 0:
            raise NonExistentUser(self.message.USERNAME_DOES_NOT_EXIST)

    def validate_email_not_unique(self, len_users):
        if len_users > 1:
            raise UserEmailNotUnique(
                self.message.MORE_THAN_ONE_USER_WITH_THE_SAME_EMAIL)