# if you need multiple conditions to be true
# this makes sure all conditions are checked instead of stopping after on e is true
# if you only want one block of code to run, use an if-elif-else statement
# if you want more than one block of code to run, use a series of independent if statements

# want multiple toppings on pizza

requested_toppings = ['mushroom', 'extra cheese']

if 'mushroom'in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
