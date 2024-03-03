# Print first, last and middle three of list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("The first three items in the list are:")
for num in list[:3]:
    print(num)

print("\nThe middle three items in the list are:")
for num in list[3:6]:
    print(num)

print("\nThe last three items in the list are:")
for num in list[-3:]:
    print(num)
