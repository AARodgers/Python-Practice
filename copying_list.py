# you use [:] to copy a list

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
# note: you can NOT do friends_foods = my_foods, this  will just assign friends_foods to the \
# my_food list, so when you append anything it will be the same list

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nM friend's favority foods are:")
print(friends_foods)
