from random import choice, randint

# Function counter to dictionary


def counter(fn: "function", count_dict: "dictionary"):
    """
    Returns a closure function that will keep count 
    of the times the passed function is called.
    Stores the records in the passed global dictionary
    """
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        count_dict[fn.__name__] = count  # No assigment, but mutability of the object
        return fn(*args, **kwargs)

    return inner


def add(x: int, y: int) -> int:
    return x + y


def substract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> float:
    return x / y


fn_count_dict = dict()
fn_count_dict_2 = dict()

add1 = counter(add, fn_count_dict)
sub1 = counter(substract, fn_count_dict)
mul1 = counter(multiply, fn_count_dict)
div1 = counter(divide, fn_count_dict)

my_functions = [add1, sub1, mul1, div1]

for i in range(100):
    choice(my_functions)(randint(1, 20), randint(1, 20))

for k in fn_count_dict.keys():
    print(f'Function "{k}" was called {fn_count_dict[k]} times')
print()

# Using closures as decorators:
add = counter(add, fn_count_dict_2)
substract = counter(substract, fn_count_dict_2)
multiply = counter(multiply, fn_count_dict_2)
divide = counter(divide, fn_count_dict_2)

my_functions_2 = [add, substract, multiply, divide]

for i in range(100):
    choice(my_functions_2)(randint(1, 20), randint(1, 20))

for k in fn_count_dict.keys():
    print(f'Function "{k}" was called {fn_count_dict_2[k]} times')

