# Function counter


def counter(fn: "function to be counted"):
    """
    Returns a closure function that will keep count 
    of the times the passed function is called and prints 
    a message with the count information.
    """
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"\n{fn.__name__} has been called {count} times")
        return fn(*args, **kwargs)

    return inner


def add(x: int, y: int):
    return x + y


add1 = counter(add)

print(add1.__code__.co_freevars)
print(add1.__closure__)
print(add1(1, 11))
print(add1(3, 1))
print(add1(5, 19))
print(add1(7, 15))
print(add1(8, 10))
