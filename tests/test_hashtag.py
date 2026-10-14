from twitter import twitter
from account import account
from post import post


def make_post(t, text, hashtag, poster):
    # so each test doesn't have to repeat these lines
    p = post(text, hashtag, poster)
    poster.posts.append(p)
    t.all_posts.append(p)
    return p


def test_finds_matching_posts():
    # get_hashtag_posts returns posts with that hashtag
    t = twitter()
    me = account("me", "pw")
    p = make_post(t, "go team", "sports", me)
    assert t.get_hashtag_posts("sports") == [p]


def test_leaves_out_other_hashtags():
    # Posts with a different hashtag are not included
    t = twitter()
    me = account("me", "pw")
    p = make_post(t, "go team", "sports", me)
    make_post(t, "yum", "food", me)
    assert t.get_hashtag_posts("sports") == [p]


def test_no_matches_is_empty():
    # Searching a hashtag nobody used returns an empty list
    t = twitter()
    me = account("me", "pw")
    make_post(t, "yum", "food", me)
    assert t.get_hashtag_posts("sports") == []


def test_case_doesnt_matter():
    # "Sports", "SPORTS", and "sports" all match each other
    t = twitter()
    me = account("me", "pw")
    p = make_post(t, "go team", "Sports", me)
    assert t.get_hashtag_posts("SPORTS") == [p]
