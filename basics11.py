# Lambda
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# Array
cars = ["Ford", "Volvo", "BMW"]
x = len(cars) # length of array
# loop in array
for x in cars:
  print(x)

# add a element
cars.append("Honda")

# remove a element
cars.pop(1) # second element
cars.remove("Volvo")

# methods in array

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list