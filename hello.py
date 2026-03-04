def greet(name):
    return f"Hello, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"


def shout(name):
    return f"HEY {name.upper()}!"


def whisper(name):
    return f"psst... {name.lower()}..."


def repeat(message, times):
    return " ".join([message] * times)


if __name__ == "__main__":
    print(greet("world"))
    print(farewell("world"))
    print(shout("world"))
    print(whisper("world"))
    print(repeat("hello", 3))
