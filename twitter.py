from account import account
from post import post

class twitter:
    pass
    def __init__(self):
        self.accounts = []
        self.current_user = None

    def create_account(self, username, password):
        pass
    def login(self, username, password):
        pass
    def logout(self):
        pass


    def make_post(self, text, hashtag):
        pass
    def follow(self, account):
        pass


    def logged_out_menu(self):
        print("Welcome to ATCS Twitter!")
        while True:
            print("1. Log in")
            print("2. Create an account")
            choice = input("Choose an option (1 or 2): ").strip()
            if choice == "1" or choice == "2":
                return choice
            print("That's not a valid option. Please enter 1 or 2.")

    def logged_in_menu(self):
        pass

    def main_loop(self):
        choice = self.logged_out_menu()
        if choice == "1":
            print("You chose to log in.")  # TODO: call self.login(...)
        else:
            print("You chose to create an account.")  # TODO: call self.create_account(...)


if __name__ == "__main__":
    twitter().main_loop()


    