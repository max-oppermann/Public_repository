from twttr import shorten

def test_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""

def test_all_cons():
    assert shorten("bbb") == "bbb"

def test_capital():
    assert shorten("CAP") == "CP"
    assert shorten("CAp") == "Cp"
    assert shorten("cAP") == "cP"

def test_punct():
    assert shorten("b.b") == "b.b"
    assert shorten("b,b") == "b,b"

def test_num():
    assert shorten("CS50P") == "CS50P"
