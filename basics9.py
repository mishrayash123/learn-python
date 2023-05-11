# while loop & continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  #############################
  # with break
  while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  # for loop
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  # for loop in string
  for x in "banana":
  print(x)

  # for loop with if 
  for x in fruits:
  print(x)
  if x == "banana":
    break

    # using range
    for x in range(6):
  print(x)

  # it's means values from 2 to 6 not including
  for x in range(2, 6):
  print(x)

  #####################################
  for x in range(2, 30, 3):
  print(x)  #The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)

  # nested loop
  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
    # pass statement
    for x in [0, 1, 2]:
       pass