from models.user import User

class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, user):
        if isinstance(user, User):
            self.users.append(user)

    def get_all_users(self):
        return self.users
