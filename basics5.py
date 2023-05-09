# touples
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#touple constructer
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

#change the touple value
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# add items in touples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# add touple to a touple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# remove element
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#unpacked touples
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# multiply touples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#methods in touple
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found