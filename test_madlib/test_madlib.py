import pytest
from madlib_cli.madlib_cli import read_template,parse_template,merge



def test_read_template():
    actual = read_template('assets/move.txt')
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected



def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected


def test_read_template_raises_exceptio():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
