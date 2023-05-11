# if else
a = 33
b = 200
if b > a:
 print("b is greater than a")

  # elif
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  # else
  if b > a:
   print("b is greater than a")
  elif a == b:
   print("a and b are equal")
  else:
   print("a is greater than b")

  # sort
  if a > b: print("a is greater than b") # ternary operators

  print("A") if a > b else print("B")

  ################################################################
  a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

  ###################################################
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

    # the pass statement
    #if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
    if b > a:
       pass