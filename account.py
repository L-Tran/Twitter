from post import post

class account:
    def __init__(self, username, password):
            self.username = username
            self.password = password
            self.followers = []
            self.following = []
            self.posts = []

    def follow(self, account):
          # You can't follow yourself or the same person twice
          if account is self or account in self.following:
                # return false for tests
                return False
          # Add account to following list add to account's followers
          self.following.append(account)
          account.followers.append(self)
          # Return true for tests
          return True

    def __repr__(self):
        return self.username