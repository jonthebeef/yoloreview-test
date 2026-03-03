from hello import greet


def test_greet():
    assert greet("world") == "Hello, world!"


def test_greet_name():
    assert greet("Jon") == "Hello, Jon!"
