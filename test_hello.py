from hello import greet, farewell


def test_greet():
    assert greet("world") == "Hello, world!"


def test_greet_name():
    assert greet("Jon") == "Hello, Jon!"


def test_farewell():
    assert farewell("world") == "Goodbye, world!"


def test_farewell_name():
    assert farewell("Jon") == "Goodbye, Jon!"
