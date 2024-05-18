# Example of recursion in python

def EvenNums(num):
  print(num)
  if num == 2:
    return num
  else:
    return EvenNums(num - 2)

EvenNums(8)
