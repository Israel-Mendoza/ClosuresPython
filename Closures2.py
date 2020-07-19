# A simple closure functions


def counter(start: int = 0):
    """Creates a counter closure function"""
    count = start

    def incrementer():
        nonlocal count
        # Increment the final object "indirectly"
        count += 1
        return count

    return incrementer


# Creating different closures:
counter_from_0 = counter()
counter_from_10 = counter(10)
counter_from_20 = counter(20)

for i in range(10):
    print(counter_from_0())

print()
for i in range(10):
    print(counter_from_10())

print()
for i in range(10):
    print(counter_from_20())
