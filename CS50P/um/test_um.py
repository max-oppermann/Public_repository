from um import count


def test_case_insensitive():
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1
    assert count("um") == 1

def test_substring():
    assert count("um album, instrument. umpire") == 1

def test_punctuation():
    assert count("um,") == 1
