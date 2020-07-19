from time import perf_counter, sleep

# Timer with classes


class Timer:
    def __init__(self):
        self._start = perf_counter()

    def __call__(self):
        return perf_counter() - self._start


t1 = Timer()
sleep(2)
print(t1())


# Timer using closures


def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


t2 = timer()
print(t2.__closure__)
sleep(2)
print(t2())
