def greet(name):
    return f"Hello, {name}!"


def farewell(name):
    return f"Goodbye, {name}!"


def shout(name):
    return f"HEY {name.upper()}!"


if __name__ == "__main__":
    print(greet("world"))
    print(farewell("world"))
    print(shout("world"))
