from post import post
class account:
    def __init__(self, username, password):
            self.username = username
            self.password = password
            self.followers = []
            self.following = []
            self.posts = []

    def post(self, text, hashtag):
        pass

    def follow(self, account):
          account.followers.append(self)

    def __repr__(self):
            pass
    