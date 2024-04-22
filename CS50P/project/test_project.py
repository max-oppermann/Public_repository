from project.project import is_due, update_date, write
from unittest.mock import patch
import pytest
from datetime import date

def test_write():
    flashcards = []
    user_inputs = ["front 1", "back 1", EOFError]

    with patch("builtins.input", side_effect=user_inputs):
        with pytest.raises(SystemExit):
            write(flashcards)
            
    assert flashcards == [{"front": "front 1", "back": "back 1", "date": date.today(), "interval": 2}]

def test_is_due():
    card1 = {"date": "3000-01-01"}
    card2 = {"date": "1000-01-01"}
    assert is_due(card1) == False
    assert is_due(card2) == True

def test_update_date():
    card = {"date": "2000-01-01", "interval": 10}
    update_date(card, True)
    assert card["date"] == date.fromisoformat("2000-01-26")
    assert card["interval"] == 25
    card = {"date": "2000-01-01", "interval": 10}
    update_date(card, False)
    assert card["date"] == date.fromisoformat("2000-01-03")
    assert card["interval"] == 2
