class post:
    def __init__(self, text, hashtag, poster):
        self.text = text
        self.hashtag = hashtag
        self.poster = poster

    def __repr__(self):
        return f"{self.poster.username} posted the following:\n {self.text} \n hashtag: {self.hashtag}"