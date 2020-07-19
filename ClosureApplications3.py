# Counter


def counter(initial_value: int):
    """
    Returns a closure function that, 
    when called, will return a integer, 
    which will increment each time the closure is called
    """

    def inner(increment: int = 1):
        nonlocal initial_value
        initial_value += increment
        return initial_value

    return inner


c1 = counter(0)
print(c1.__closure__)
print(c1())
print(c1())
print(c1(10))
