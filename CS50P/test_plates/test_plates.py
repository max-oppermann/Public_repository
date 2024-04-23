from plates import is_valid


def test_letters_start():
    assert is_valid("2A") in [False, None]
    assert is_valid("A2") in [False, None]

def test_two_to_six():
    assert is_valid("A") in [False, None]
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAAA") == True
    assert is_valid("AAAAA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AAAAAAA") in [False, None]

def test_no_middle_num():
    assert is_valid("AAA22A") in [False, None]

def test_alpha_numeric():
    assert is_valid("AAAA.") in [False, None]
    assert is_valid("AAAA,") in [False, None]
    assert is_valid("AA:;?!") in [False, None]

def test_no_spaces():
    assert is_valid("AAAA A") in [False, None]

def test_first_num_zero():
    assert is_valid("AAA022") in [False, None]

