# Introspecting the functions


def outer():
    x = "Python"
    y = "Java"

    def inner():
        # "x" and "y" are free variables because they were not defined locally
        print(f'My languages: "{x}" and "{y}"')

    return inner


fn = outer()  # Assigning the closure to a variable

# Print the free variables of the closure
print(f"fn's free variables: {fn.__code__.co_freevars}")
# Print the closure information (cell and indirect objects)
print(f"fn's closure information: {fn.__closure__}")
# Running the closure:
fn()
