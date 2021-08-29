from app import db
from tests.data.login_constants import LoginConstants
from entities import User


class FixtureUser():

    def clear():
        db.session.query(User).delete()
        db.session.commit()

    def run():
        login_constant = LoginConstants()
        user = User(login_constant.EXISTING_EMAIL, login_constant.USER_NAME, login_constant.HOUR_PRICE, login_constant.PROFIT, login_constant.IMAGE_URL)
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
