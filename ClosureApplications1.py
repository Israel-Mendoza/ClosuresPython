# Average returner with classes


class Averager:
    def __init__(self):
        self._total = 0
        self._count = 0

    @property
    def total(self):
        return self._total

    @property
    def count(self):
        return self._count

    def add(self, number: int):
        self._total += number
        self._count += 1
        return self.total / self.count


a = Averager()

print(a.__class__)
print(a.add(10))
print(a.add(15))
print(a.add(30))
print()


# Average returner with functions


def averager():
    total = 0
    count = 0

    def inner(x: int):
        nonlocal total, count
        total += x
        count += 1
        return total / count

    return inner


a = averager()

print(a.__closure__)
print(a(10))
print(a(15))
print(a(30))
print()

