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

my_pizzas = ['margarita', 'cheese', 'pepperoni', 'vegetable']
friend_pizza = my_pizzas[:]
my_pizzas.append('meat lovers')
friend_pizza.append('pineapple')
print("My favorite pizzas are:")
for pizza in my_pizzas:
  print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)
