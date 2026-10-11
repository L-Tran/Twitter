import sys
from account import account
from post import post

class twitter:
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
        # Tell the user why the follow didn't work, or confirm it did
        if account is self.current_user:
            print("You can't follow yourself")
        elif not self.current_user.follow(account):
            print("You already follow " + account.username)
        else:
            print("You are now following " + account.username)

    def who_to_follow(self):
        # Everyone except yourself and people you already follow
        options = []
        # Find all accounts that aren't you or your following
        for acc in self.accounts:
            if acc is not self.current_user and acc not in self.current_user.following:
                options.append(acc)

        if len(options) == 0:
            print("There is nobody new to follow right now.")
            return
        
        # Print options
        for i in range(len(options)):
            print(str(i + 1) + ". " + options[i].username)

        # Pick a number to follow them, or go back
        choice = input("Enter a number to follow them, or press Enter to go back: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            self.follow(options[int(choice) - 1])
        elif choice != "":
            print("That's not a valid option.")

    def valid_menu_choice(self, choice):
        # Returns True if the choice is "1" or "2" (spaces ignored)
        return choice.strip() == "1" or choice.strip() == "2"

    # Main menu function / what user sees when logged out
    def logged_out_menu(self):
        print("Welcome to ATCS Twitter!")
        # Ensure user chooses a proper option
        while True:
            print("1. Log in")
            print("2. Create an account")
            choice = input("Choose an option (1 or 2): ").strip()
            # Only leave the loop once the choice is valid
            if self.valid_menu_choice(choice):
                return choice
            print("That's not a valid option. Please enter 1 or 2.")

    # Show posts one at a time until the user types 'back' or runs out of posts
    # Abstraction for both view post functions
    # I thought of the abstraction AI helped me think of how to transfer the messages by passing them through parameters
    def show_posts(self, posts, empty_message, done_message, allow_profile=True):
        if len(posts) == 0:
            print(empty_message)
            return

        for p in posts:
            print(p)
            # Keep asking about this post until the user moves on or goes back
            while True:
                if allow_profile:
                    prompt = "Press Enter for the next post, type 'profile' to view " + p.poster.username + "'s profile, or 'back' to return to the menu: "
                else:
                    prompt = "Press Enter for the next post, or type 'back' to return to the menu: "
                choice = input(prompt).strip().lower()
                if choice == "back":
                    return
                elif choice == "profile" and allow_profile:
                    self.view_profile(p.poster)
                elif choice == "":
                    break
                else:
                    print("That's not a valid option.")
        print(done_message)

    def view_profile(self, account):
        # Show an account's info, then let the user browse their posts or follow them
        while True:
            print("--- " + account.username + "'s profile ---")
            print("Followers: " + str(len(account.followers)) + " | Following: " + str(len(account.following)) + " | Posts: " + str(len(account.posts)))
            if account is not self.current_user:
                if account in self.current_user.following:
                    print("You follow this person.")
                else:
                    print("You don't follow this person.")
            # Only offer follow if it's someone else you don't follow yet
            can_follow = account is not self.current_user and account not in self.current_user.following
            print("1. View posts")
            if can_follow:
                print("2. Follow")
            back = "3" if can_follow else "2"
            print(back + ". Back")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                # Newest first; no profile option since we're already here
                self.show_posts(list(reversed(account.posts)), account.username + " hasn't posted anything yet.",
                                "You have seen all of " + account.username + "'s posts!", allow_profile=False)
            elif choice == "2" and can_follow:
                self.follow(account)
            elif choice == back:
                return
            else:
                print("That's not a valid option.")

    def view_feed(self):
        # Collect posts from people current user follows, newest first
        feed = []
        # Reverse for newest first AI helped come up with it
        for p in reversed(self.all_posts):
            if p.poster in self.current_user.following:
                feed.append(p)
        return feed

    def view_feed(self):
        self.show_posts(self.get_feed(), "There are no posts from people you follow yet.", "You are up to date!")

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

    # Homepage / what the user sees when logged in
    def logged_in_menu(self):
        # Ensure user chooses valid option
        while True:
            print("1. View feed")
            print("2. Search hashtag")
            print("3. Post")
            print("4. Who to follow")
            print("5. Log out")
            print("6. Close program")
            choice = input("Choose an option (1-6): ").strip()
            # Execute user's choice
            if choice == "1":
                self.view_feed()
            elif choice == "2":
                self.search_hashtag()
            elif choice == "3":
                self.post()
            elif choice == "4":
                self.who_to_follow()
            elif choice == "5":
                self.logout()
                return
            elif choice == "6":
                print("Goodbye!")
                sys.exit()
            else:
                print("That's not a valid option. Please enter an option 1-6.")

    def main_loop(self):
        while True:
            # Initialize main menu
            choice = self.logged_out_menu()
            # Execute user choice
            if choice == "1":
                print("You chose to log in.")
                self.login()
            else:
                print("You chose to create an account.")
                self.create_account()
            if self.current_user is not None:
                self.logged_in_menu()

if __name__ == "__main__":
    twitter().main_loop()
