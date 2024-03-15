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

