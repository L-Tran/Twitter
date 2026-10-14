from twitter import twitter
from account import account
from post import post


def make_post(t, text, hashtag, poster):
    # so each test doesn't have to repeat these lines
    p = post(text, hashtag, poster)
    poster.posts.append(p)
    t.all_posts.append(p)
    return p


def test_post_stores_text_hashtag_and_poster():
    # A post remembers its text, hashtag and who made it
    me = account("me", "pw")
    t = twitter()
    p = make_post(t, "hello", "greetings", me)
    assert p.text == "hello"
    assert p.hashtag == "greetings"
    assert p.poster is me


def test_post_prints_username_and_text():
    # Printing a post shows who posted it and what it said
    me = account("me", "pw")
    t = twitter()
    p = make_post(t, "hello", "greetings", me)
    assert "me" in str(p)
    assert "hello" in str(p)


def test_posts_are_added_in_order():
    # Newer posts go at the end of all_posts and the poster's posts
    t = twitter()
    me = account("me", "pw")
    first = make_post(t, "first", "", me)
    second = make_post(t, "second", "", me)
    assert t.all_posts == [first, second]
    assert me.posts == [first, second]
