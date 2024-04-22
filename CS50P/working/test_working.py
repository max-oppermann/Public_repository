import pytest
from working import convert

def test_AM_PM():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"

def test_sixty_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        convert("13:00 AM to 5:00 PM")
        convert("9:00 AM to 13:00 PM")

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
