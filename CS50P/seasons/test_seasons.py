from seasons import get_bday
from seasons import date_to_words
import pytest

def test_format():
    assert date_to_words(1) == "One"

