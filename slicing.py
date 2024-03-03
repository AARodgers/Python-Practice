# Slicing: to output the first three items in a list, you would request indices 0-3
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#print last three elements in list
print(players[-3:])

# a third value lets you skip elements, this will give you the 0 and 2 element
print(players[0:4:2])

#loop a slice with a for loop, ex. loop through first three elements and print the names
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
