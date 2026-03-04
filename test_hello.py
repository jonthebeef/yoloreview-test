from hello import greet, farewell, shout, whisper, repeat


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


def test_whisper():
    assert whisper("World") == "psst... world..."


def test_repeat():
    assert repeat("hi", 3) == "hi hi hi"
