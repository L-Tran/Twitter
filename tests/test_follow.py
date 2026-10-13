from twitter import twitter
from account import account


def test_follow_adds_to_both_lists():
    # Following someone puts them in my following list and me in their followers list
    me = account("me", "pw")
    friend = account("friend", "pw")
    assert me.follow(friend) == True
    assert me.following == [friend]
    assert friend.followers == [me]


def test_cant_follow_yourself():
    # account.follow returns False and changes nothing if you follow yourself
    me = account("me", "pw")
    assert me.follow(me) == False
    assert me.following == []
    assert me.followers == []


def test_cant_follow_twice():
    # Following the same person twice only counts once
    me = account("me", "pw")
    friend = account("friend", "pw")
    me.follow(friend)
    assert me.follow(friend) == False


def test_follow_is_one_way():
    # If I follow friend, friend does not automatically follow me
    me = account("me", "pw")
    friend = account("friend", "pw")
    me.follow(friend)
    assert friend.following == []
    assert me.followers == []
