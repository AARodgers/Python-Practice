#use range() to make a list of numbers
for value in range(1, 5):
    print(value)
# this prints 1, 2, 3, 4, the range stops when it gets to 5

# this will print 0-5
for value in range(6):
    print(f"New set:{value}")

# list() converts a set of numbers into a list
numbers = list(range(1,6))
print(numbers)

#list even numbers between 1 and 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#print a list of the square of the numbers 1-10
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
# OR this does the same thing, just more concise
squares2 = []
for value in range(1, 11):
    squares2.append(value ** 2)
print(squares2)
