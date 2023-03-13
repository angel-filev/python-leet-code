from myproject.services.user_service import UserService
from myproject.models.user import User

def main():
    # Initialize the user service
    user_service = UserService()

    # Create a new user
    user = User(username="johndoe", email="johndoe@example.com")
    user_service.create_user(user)

    # Retrieve all users and print their usernames
    users = user_service.get_all_users()
    for user in users:
        print(user.username)

if __name__ == '__main__':
    main()
