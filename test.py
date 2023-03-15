from project import format_input
from project import experience
from project import format_table
import pytest


def main():
    test_format_input()
    test_experience()
    # test_routine()


def test_format_input():
    assert format_input("1") == 1.0
    assert format_input("one") == 1
    assert format_input("2.9") == 2.9
    assert format_input("2.9.") == 2.9
    assert format_input("three point six") == 3.6
    assert format_input("1 year") == 1.0
    assert format_input("two years") == 2
    assert format_input("I have trained for two years") == 2
    assert format_input("i HAVE, worked out for nine years") == 9
    with pytest.raises(SystemExit):
        format_input("-1")
    with pytest.raises(SystemExit):
        format_input("cat")
    with pytest.raises(SystemExit):
        format_input("")
    with pytest.raises(SystemExit):
        format_input("CS50")


def test_experience():
    assert experience(0) == "novice"
    assert experience(1) == "novice"
    assert experience(0.6) == "novice"
    assert experience(1.01) == "intermediate"
    assert experience(2) == "intermediate"
    assert experience(3) == "intermediate"
    assert experience(4) == "advanced"
    assert experience(5) == "advanced"
    assert experience(100) == "advanced"
    assert experience(122) == "advanced"
    with pytest.raises(SystemExit):
        experience(123)


# def test_routine():
#     assert routine("novice" = )


if __name__ == "__main__":
    main()
