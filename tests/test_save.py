import os
import twitter as twitter_module
from twitter import twitter
from account import account
from post import post

TEST_FILE = "test_save_file.json"


def make_post(t, text, hashtag, poster):
    # so each test doesn't have to repeat these lines
    p = post(text, hashtag, poster)
    poster.posts.append(p)
    t.all_posts.append(p)
    return p


def make_saved_twitter():
    # bob follows al and has one post, saved to a test file
    twitter_module.SAVE_FILE = TEST_FILE
    t = twitter()
    bob = account("bob", "pw1")
    al = account("al", "pw2")
    bob.follow(al)
    t.accounts = [bob, al]
    make_post(t, "hi", "tag", bob)
    t.save()
    return t


def test_load_restores_accounts():
    # Usernames and passwords survive a save and load
    make_saved_twitter()
    t = twitter()
    assert t.load() == True
    assert t.accounts[0].username == "bob"
    assert t.accounts[0].password == "pw1"
    assert t.accounts[1].username == "al"
    os.remove(TEST_FILE)


def test_load_restores_follows():
    # Following and followers are rebuilt
    make_saved_twitter()
    t = twitter()
    t.load()
    bob, al = t.accounts
    assert bob.following == [al]
    assert al.followers == [bob]
    os.remove(TEST_FILE)


def test_load_restores_posts():
    # Posts come back in all_posts and on the poster's account
    make_saved_twitter()
    t = twitter()
    t.load()
    p = t.all_posts[0]
    assert p.text == "hi"
    assert p.hashtag == "tag"
    assert t.accounts[0].posts == [p]
    os.remove(TEST_FILE)


def test_load_without_save_returns_false():
    # No save file means load fails and nothing is added
    twitter_module.SAVE_FILE = "does_not_exist.json"
    t = twitter()
    assert t.load() == False
    assert t.accounts == []
