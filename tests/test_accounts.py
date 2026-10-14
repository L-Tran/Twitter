from twitter import twitter
from account import account


def test_account_stores_username_and_password():
    # A new account remembers what it was created with
    me = account("me", "pw")
    assert me.username == "me"
    assert me.password == "pw"


def test_twitter_starts_logged_out():
    # A new twitter has no accounts and nobody logged in
    t = twitter()
    assert t.accounts == []
    assert t.current_user is None


def test_logout_clears_current_user():
    # logout sets the current user back to None
    t = twitter()
    t.current_user = account("me", "pw")
    t.logout()
    assert t.current_user is None
