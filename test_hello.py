from hello import greet, farewell, shout


def test_greet():
    assert greet("world") == "Hello, world!"


def test_greet_name():
    assert greet("Jon") == "Hello, Jon!"


def test_farewell():
    assert farewell("world") == "Goodbye, world!"


def test_farewell_name():
    assert farewell("Jon") == "Goodbye, Jon!"


def test_shout():
    assert shout("world") == "HEY WORLD!"


def test_shout_name():
    assert shout("Jon") == "HEY JON!"
