from twitter import twitter
from account import account
from post import post


def make_post(t, text, poster):
    # so each test doesn't have to repeat these lines
    p = post(text, "", poster)
    poster.posts.append(p)
    t.all_posts.append(p)
    return p


def test_shows_followed_posts():
    # get_feed returns posts from accounts you follow
    t = twitter()
    me = account("me", "pw")
    friend = account("friend", "pw")
    t.current_user = me
    me.follow(friend)
    p = make_post(t, "hello", friend)
    # The feed should have exactly that one post
    assert t.get_feed() == [p]


def test_hides_unfollowed_posts():
    # get_feed leaves out posts from accounts you don't follow
    t = twitter()
    me = account("me", "pw")
    stranger = account("stranger", "pw")
    t.current_user = me
    # "stranger" makes a post, but I do not follow them
    make_post(t, "you can't see me", stranger)
    # So the feed should be empty
    assert t.get_feed() == []


def test_newest_first():
    # get_feed returns the newest post first
    t = twitter()
    # Make two accounts
    me = account("me", "pw")
    friend = account("friend", "pw")
    t.current_user = me
    me.follow(friend)
    # "friend" posts twice: first "old post", then "new post"
    old = make_post(t, "old post", friend)
    new = make_post(t, "new post", friend)
    # The feed should show the new post first, then the old one
    assert t.get_feed() == [new, old]


def test_empty_when_following_nobody():
    # get_feed returns an empty list if you follow nobody
    t = twitter()
    me = account("me", "pw")
    t.current_user = me
    # me follows nobody, so the feed should be empty
    assert t.get_feed() == []
