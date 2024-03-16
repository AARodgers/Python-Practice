#will execute one block, it runs each conditional test in order until one passes
# if on condition passes it executes the code after that condition and skips the rest
# note: it does not require an else at the end of elif statement

# Ex.Admission to theme park varies for different ages
age = 12
if age < 4:
  print("Your admission cost is $0.")
elif age < 18:
  print("Your admission cost is $25.")
else:
  print("Your admission cost is $40.")

# can also write like this

  age = 12

  if age < 4:
    price = 0
  elif age < 18:
    price = 25
  elif age < 65:
    price = 40
  else:
    price = 20

  print(f"Your admission cost is ${price}.")

# can  write witout and else block, can be safer because it is more specific

age = 12

if age < 4:
  price = 0
elif age < 18:
  price = 25
elif age < 65:
  price = 40
elif age >= 65:
  price = 20

print(f"Your admission cost is ${price}.")
