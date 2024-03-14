# tuples are immutable list, you can't change the items in them
# they are defined by the comma so if you generate a tuple with one item it will be (1,)
# you can't modify a tuple but can assign new values to the variable that defines the tuple
# (your just reassigning the variable)

# a square with dimensions that should never change
dimensions = (200, 5)
print(dimensions[0])
for dimension in dimensions:
    print(dimension)

#tuple with one item
my_t = (3,)

#
