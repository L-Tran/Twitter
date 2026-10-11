from account import account
from post import post

class twitter:
    pass
    def __init__(self):
        self.accounts = []
        self.current_user = None
        self.all_posts = []  # every post ever made, oldest first

    def create_account(self):
        # Ask for a username until it is non-empty and not already taken
        while True:
            username = input("Please enter the username for your new account: ").strip()
            if username == '':
                print("You need to have something for your username")
            elif any(acc.username == username for acc in self.accounts):
                print("You need a unique username")
            else:
                break

        # Ask for a password until it is non-empty
        while True:
            password = input("Please enter the password for your new account: ")
            if password == '':
                print("You need to have a password")
            else:
                break

        # Create the account, save it, and log the user into it
        self.accounts.append(account(username, password))
        print("you are now logged in to the new account")
        self.current_user = self.accounts[-1]

    def login(self):
        # Ask for credentials and log in if an account matches both
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ")
        for acc in self.accounts:
            if acc.username == username and acc.password == password:
                self.current_user = acc
                return
        # No account matched, so nobody is logged in
        print("There is no account with that username and password")

    def logout(self):
        # No current user means we are logged out
        self.current_user = None

    def post(self):
        # Ask for the post text until it is non-empty
        while True:
            text = input("What do you want to post? ").strip()
            if text != '':
                break
            print("Your post can't be empty")
        # Hashtag is optional (empty string if skipped)
        hashtag = input("What's the hashtag? (optional, press enter if you don't want it)")
        # Save the post on the user's account and in the global list used by feeds
        this_post = post(text, hashtag, self.current_user)
        self.current_user.posts.append(this_post)
        self.all_posts.append(this_post)

        
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
            print("3. Post")
            choice = input("Choose an option (1-3): ").strip()
            if choice == "1":
                self.view_feed()
            elif choice == "2":
                self.logout()
                return
            elif choice == "3":
                self.post()
            else:
                print("That's not a valid option. Please enter an option 1-3.")

    def main_loop(self):
        while True:
            
            choice = self.logged_out_menu()
            if choice == "1":
                print("You chose to log in.")
                self.login()
            else:
                print("You chose to create an account.")  # TODO: call self.create_account(...)
                self.create_account()
            if self.current_user is not None:
                self.logged_in_menu()

if __name__ == "__main__":
    twitter().main_loop()


    