from numb3rs import validate

def test_small():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False

def test_four_groups():
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False

def test_digits():
    assert validate("a.1.1.1") == False
    assert validate("1.a.1.1") == False
    assert validate("1.1.a.1") == False
    assert validate("1.1.1.a") == False




'''
testing
there are 4 groups
they are all digits (ints)
they are less than 256
'''
