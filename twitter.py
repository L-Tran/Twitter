from account import account
from post import post

class twitter:
    pass
    def __init__(self):
        self.accounts = []
        self.current_user = None
        self.all_posts = []  # every post ever made, oldest first

    def create_account(self):
        try:
            username = input("Please enter the username for your new account:")
        except any([username == account.username for account in self.accounts]):
            print("You need a unique username")
        password = input("Please enter the password for your new account:")
        self.accounts.append(account(username, password))
        print("you are now logged in to the new account")
        self.login(username, password)

    def login(self, username, password):
        #for account in accounts:
        pass

    def logout(self):
        pass


    def make_post(self, text, hashtag):
        pass
    def follow(self, account):
        self.current_user.follow(account)


    def logged_out_menu(self):
        print("Welcome to ATCS Twitter!")
        while True:
            print("1. Log in")
            print("2. Create an account")
            choice = input("Choose an option (1 or 2): ").strip()
            if choice == "1" or choice == "2":
                return choice
            print("That's not a valid option. Please enter 1 or 2.")

    def view_feed(self):
        # Collect posts from people I follow, newest first
        feed = []
        for p in reversed(self.all_posts):
            if p.poster in self.current_user.following:
                feed.append(p)

        # Show one post at a time
        for p in feed:
            print(p)
            choice = input("Press Enter for the next post, or type 'back' to return to the menu: ").strip().lower()
            if choice == "back":
                return
        print("You are up to date!")

    def logged_in_menu(self):
        while True:
            print("1. View feed")
            print("2. Log out")
            choice = input("Choose an option (1 or 2): ").strip()
            if choice == "1":
                self.view_feed()
            elif choice == "2":
                self.logout()
                return
            else:
                print("That's not a valid option. Please enter 1 or 2.")

    def main_loop(self):
        choice = self.logged_out_menu()
        if choice == "1":
            print("You chose to log in.")  # TODO: call self.login(...)
        else:
            print("You chose to create an account.")  # TODO: call self.create_account(...)
            self.create_account()

if __name__ == "__main__":
    twitter().main_loop()


    