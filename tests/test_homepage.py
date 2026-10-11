from twitter import twitter


def test_1_is_valid():
    # valid_menu_choice("1") returns True
    t = twitter()
    assert t.valid_menu_choice("1") == True


def test_2_is_valid():
    # valid_menu_choice("2") returns True
    t = twitter()
    assert t.valid_menu_choice("2") == True


def test_other_choices_are_invalid():
    # valid_menu_choice returns False for things like "3", "", "abc"
    t = twitter()
    assert t.valid_menu_choice("3") == False
    assert t.valid_menu_choice("") == False
    assert t.valid_menu_choice("abc") == False


def test_spaces_are_ignored():
    # valid_menu_choice(" 1 ") returns True
    t = twitter()
    assert t.valid_menu_choice(" 1 ") == True
