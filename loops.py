# basic for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# for loop with message for each item
# note: everything indented will occur once to each item in list
# once you don't indent something the loop is done and it will execute once
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")
print("Thank you, magicians. That was a great show!")

my_fav_pizzas = ['supreme', 'veggie', 'meat lovers']
for pizza in my_fav_pizzas:
    print(f"\n{pizza.title()} is one of my favorite pizzas")
print("\nI like all kinds of pizzas.")
