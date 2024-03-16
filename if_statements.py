#if conditional_test:
#    do something
# ( if conditional_test evaluates to true, the program will execute the code on the )\
# next line, if the conditional_test evaluates to false, it will ignore the code on the \
#next line

age = 19
if age >= 18:
   print("You are old enough to vote.")
   print("Have you registered to vote?")

# loop through cars to make them capitalized but when you hit bmw, capitalize every letter
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car.title())

#Checking for eqaulity

#sets value of car to 'bmw'
car = 'bmw'
# equality operator returns true if values on the left and right side of operator \
# are the same
car == 'bmw'
# returns true
car == 'audi'
# returns false

#is case sensitive
car = 'bmw'
car == 'Bmw'
#false
car = "Audi"
car.lower() == 'audi'
#True
#won't affect the original value
car = "Audi"

# inequality operator
requested_topping = 'mushroom'
if requested_topping != 'anchoives':
    print("Hold the anchovies")

answer = 17
if answer != 42:
    print("That is not the right answer.")

#checking for multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
#false
# you can use parentheses as well
(age_0 >= 21) and ( age_1 >= 21)

# using or, will result in true if one or the other test pass
(age_0 >= 21) or ( age_1 >= 21)
#true

#check to see if a item is in a list
requested_topping = ['pineapple', 'onion', 'olive']
'mushroom' in requested_topping
#false
'pineapple' in requested_topping
#true

#checking to see if an item is not in list. ex. a banned user in a forum
banned_users = ['Bob', 'Sam', 'Ty']
user = 'Marie'
if user not in banned_users:
    print(f"{user.title()}, you may post on the blog.")

#booleans
game_active = True
can_edit = False
