#use a for loop to print nums 1-20
# note: if you loop through too many numbers and it is taking too long, hit Ctrl C or close \
# output window
for number in range(1, 21):
    print(number)

# min, max, and sum of nums from 1-million
one_million = list(range(1, 1_000_001))
print(min(one_million))
print(max(one_million))
print(sum(one_million))

#print odd numbers from 1-20
for number in range(1, 21, 2):
    print(number)

# list of multiples of 3 from 3-30
for number in range(3, 31, 3):
    print(number)

# the cube of numbers 1-10
for number in range(1, 11):
    print(number**3)
