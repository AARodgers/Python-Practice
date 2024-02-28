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
