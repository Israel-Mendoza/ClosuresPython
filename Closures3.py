# Caveats concerning the creation of the intermediary cell object


# Empty list to contain the adder closures
my_adders = []

# The following loop will not append "closures" to the "my_adders" list
# because "num" is a gobal variable, therefore no itermediary cell object is created
for num in range(1, 4):
    my_adders.append(lambda x: x + num)

# Testing each of the adders with a loop
for adder in my_adders:
    print(adder(10))  # -> 13, 13, 13 (global n ends up being 3)

# Checking the closure on each adder with the __closure__ method
for adder in my_adders:
    # None, None, None (the adder is not a closure because n is global)
    print(adder.__closure__)


########################################################################################
########################################################################################

# Clear my list
my_adders.clear()

# Defining a function to create closures and append them to the list
def adder_list_creator(add_list: list, num: int):
    """Runs a loop 'num' times and adds an adder closure to the passed list"""
    for n in range(1, num + 1):
        # "n" will always point to the same cell object
        add_list.append(lambda x: x + n)


adder_list_creator(my_adders, 3)

# Testing each of the adders with a loop
# The free variable in all closures in the list point to the same cell object
for adder in my_adders:
    print(adder(10))  # -> 13, 13, 13

# Checking the closure on each adder with the __closure__ method
for adder in my_adders:
    print(adder.__closure__)  # -> cell, cell, cell (same cell all the time)
print()

########################################################################################
########################################################################################

my_adders.clear()

# Defining a function to create closures and append them to the list
def adder_appender(adder_list: list, num: int):
    """Appends an adder with 'num' as the free variable"""
    adder_list.append(lambda x: x + num)


# Looping to add adders to the "my_adders"
for i in range(1, 4):
    adder_appender(my_adders, i)

# Testing each of the adders with a loop
for adder in my_adders:
    print(adder(10))  # -> 11, 12, 13

# Checking the closure on each adder with the __closure__ method
for adder in my_adders:
    # cell, cell, cell (Different cell objects all the time)
    print(adder.__closure__)
print()

########################################################################################
########################################################################################
# Clear the list
my_adders.clear()


def create_adder(num_to_add):
    return lambda number: number + num_to_add


for i in range(1, 10):
    my_adders.append(create_adder(i))

# Testing the adders

for adder in my_adders:
    print(f"Adding 10 to current adder: {adder(10)}")  # 11, 12, 13...
print()


for adder in my_adders:
    # cell, cell, cell (Different cell objects all the time)
    print(adder.__closure__)
print()
