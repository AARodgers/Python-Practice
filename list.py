colors = ['red', 'yellow', 'purple', 'orange']

# first color
print(colors[0])

#first color capitalized
print(colors[0].title())

#last item of list
print(colors[-1])

#second to last item in list
print(colors[-2])

message = f"My second favorite color is {colors[2].title()}."
print(message)

#change the value of an element in the list
colors[2] = 'blue'
print(colors)

#appending elements to the end of the list
colors.append('purple')
print(colors)

#user append to make a new list
new_list = []
new_list.append('one')
new_list.append('two')
new_list.append('three')
print(new_list)

'''
#insert a new value into the list, .insert(position, value), it will shift the other values \
to the right
'''
new_list.insert(0, 0.5)
print(new_list)
new_list.insert(2, 1.5)
print(new_list)

# removing an item from a list using del if you know the position of it, you can no longer \
#access that value
furniture = ['chair', 'table', 'couch', 'desk']
del furniture[0]
print(furniture)

# popping the last item off of a list using .pop(), you can then use it's value
popped_furniture = furniture.pop()
print(popped_furniture)

#popping items from any position in a list
numbers = [1, 2, 3, 4]
print(numbers)
second_number = numbers.pop(1)
print(second_number)

#to remove an item use .remove(item)
# note: .remove('item') only removes the FIRST occurance of the value specified, you a loop \
# if you want to remove all of them
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#OR
furniture = ['chair', 'table', 'couch', 'desk']
print(furniture)
too_old = 'chair'
furniture.remove(too_old)
print(furniture)
print(f"\nA {too_old.title()} is too old to keep.")

# use sorted(list) to maintain the original order of a list and to present it in a sorted order
# can do print(sorted(cars, reverse=True)) to get it in reverse order
# note: it doesn't alwasy work if you have a mix of upper and lower case numbers
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the origin list of cars:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

'''
#use .reverse() to reverse chronological order, ex. chronological order of when you owned cars
# list.reverse() to reverse the order of the list
# note: list.reverse() permanently changes order of list, but you can revert to original \
#by calling .reverse() on it again
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nOriginal list of:")
print(cars)
cars.reverse()
print("\nReversed list of cars:")
print(cars)

# use len(list) to find the length of a list
print(f"\nThe length of the list of cars is {len(cars)} ")
