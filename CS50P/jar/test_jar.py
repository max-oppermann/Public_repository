from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar = Jar("one")
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(1)
    with pytest.raises(ValueError):
        jar.deposit(2)


def test_withdraw():
    jar = Jar(3)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)
