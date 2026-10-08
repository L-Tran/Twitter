from account import account
from post import post

class twitter:
    pass
    def __init__(self):
        self.accounts = []
        self.current_user = None
        self.all_posts = []  # every post ever made, oldest first

    def create_account(self):
        while True:
            username = input("Please enter the username for your new account: ").strip()
            if username == '':
                print("You need to have something for your username")
            elif any(acc.username == username for acc in self.accounts):
                print("You need a unique username")
            else:
                break

        while True:
            password = input("Please enter the password for your new account: ")
            if password == '':
                print("You need to have a password")
            else:
                break

        self.accounts.append(account(username, password))
        print("you are now logged in to the new account")
        self.current_user = self.accounts[-1]

    def login(self):
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ")
        for acc in self.accounts:
            if acc.username == username and acc.password == password:
                self.current_user = acc
                return
        print("There is no account with that username and password")

    def logout(self):
        self.current_user = None


    def make_post(self, text, hashtag):
        pass

    def follow(self, account):
        self.current_user.follow(account)

    # Main menu function / what user when logged out
    def menu(self):
        print("Welcome to ATCS Twitter!")
        # Ensure user chooses a proper option
        while True:
            print("1. Log in")
            print("2. Create an account")
            choice = input("Choose an option (1 or 2): ").strip()
            if choice == "1" or choice == "2":
                return choice
            print("That's not a valid option. Please enter 1 or 2.")

    # Show posts one at a time until the user types 'back' or runs out of posts
    # Abstraction for both view post functions
    # I thought of the abstraction AI helped me think of how to transfer the messages by passing them through parameters
    def show_posts(self, posts, empty_message, done_message):
        if len(posts) == 0:
            print(empty_message)
            return

        for p in posts:
            print(p)
            # Enter will keep showing posts
            choice = input("Press Enter for the next post, or type 'back' to return to the menu: ").strip().lower()
            if choice == "back":
                return
        print(done_message)

    def view_feed_followers(self):
        # Collect posts from people current user follows, newest first
        feed = []
        # Reverse for newest first AI helped come up with it
        for p in reversed(self.all_posts):
            if p.poster in self.current_user.following:
                feed.append(p)

        self.show_posts(feed, "There are no posts from people you follow yet.", "You are up to date!")

    # AI helped with lstrip to get the # away
    def search_hashtag(self):
        # Get the hashtag without the # case doesn't matter
        tag = input("Enter a hashtag to search (without the #): ").strip().lstrip("#").lower()

        # Collect posts with an exact match on the hashtag, newest first
        results = []
        for p in reversed(self.all_posts):
            if p.hashtag is not None and p.hashtag.strip().lstrip("#").lower() == tag:
                results.append(p)

        self.show_posts(results, "There are no posts with #" + tag, "You have seen all posts with #" + tag + "!")

    # Homepage / what the user sees when logged out
    def homepage(self):
        # Ensure user chooses valid option
        while True:
            print("1. View feed")
            print("2. Search hashtag")
            print("3. Log out")
            choice = input("Choose an option (1, 2, or 3): ").strip()
            # Execute user's choice
            if choice == "1":
                self.view_feed_followers()
            elif choice == "2":
                self.search_hashtag()
            elif choice == "3":
                self.logout()
                return
            else:
                print("That's not a valid option. Please enter 1, 2, or 3.")

    def main_loop(self):
        while True:
            # Initialize main menu
            choice = self.menu()
            # Execute user choice
            if choice == "1":
                print("You chose to log in.")
                self.login()
            else:
                print("You chose to create an account.")
                self.create_account()
            if self.current_user is not None:
                self.homepage()

if __name__ == "__main__":
    twitter().main_loop()


    