from app import db
from tests.data.login_constants import LoginConstants
from entities import User


class FixtureUserNameNotUnique():

    def clear():
        db.session.query(User).delete()
        db.session.commit()

    def run():
        login_constant = LoginConstants()
        user = User(login_constant.EMAIL_NOT_UNIQUE, login_constant.PASSWORD_VALID_ENCRYPTED, login_constant.USER_NAME, login_constant.HOUR_PRICE, login_constant.PROFIT, login_constant.IMAGE_URL)
        user_with_the_same_user_name = User(login_constant.EMAIL_USER_NAME_UNIQUE, login_constant.PASSWORD_VALID_ENCRYPTED, login_constant.USER_NAME, login_constant.HOUR_PRICE, login_constant.PROFIT, login_constant.IMAGE_URL)
        db.session.add(user)
        db.session.add(user_with_the_same_user_name)
        db.session.commit()
        db.session.refresh(user)