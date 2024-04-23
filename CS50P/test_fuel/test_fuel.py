import pytest
from fuel import convert, gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_integer():
    with pytest.raises(ValueError):
        convert("one/2")
        convert("1/two")
        convert("one/two")
        convert("1.0/2")
        convert("1/2.0")
        convert("-1/2")
        convert("1/-2")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"

def test_less_hundred():
    with pytest.raises(ValueError):
        convert("4/3")

def test_correct_answer():
    assert convert("4/10") == 40

