from entities import User

class RepositoryUser():
    def find_users_by_email(self, email):
        users = User.query.filter_by(email=email).all()
        return users

    def find_user_by_email(self, email):
        user = User.query.filter_by(email=email).one_or_none()
        return user
    
    def get_all(self):
        users = User.query.all()
        return users