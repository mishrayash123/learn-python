print("hello world") #hello world printing
print("hello\nI am yash kumar mishra\n from bareilly") #print in new line

"""
print("njnknk")
print("kjjiokji")

"""
print("hello\nI am \"yash\" kumar mishra\n from bareilly") # " " print karna

print("jj",6,8787979, "ojo", sep="~", end="989\n")
print("yash")
 
 # datatypes
a=23
print(a)
print(type(a))
 
list1=[8,3,"oke"]
print(list1)
print(len(list1))

#list constructer
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Negative Indexing
# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#insert item
thislist.insert(2, "watermelon")
print(thislist)
#Change the second and third value by replacing it with one value
thislist[1:3] = ["watermelon"]
print(thislist)
# reolace the values
thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)
# extend list
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#remove element
thislist.remove("banana")
thislist.pop(1)
del thislist[0]
#remove last item
thislist.pop()
#clear list
thislist.clear()
#if condition
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# sorting
fruits.sort()
thislist.sort(reverse = True) # in descending
thislist.reverse() #reverse
 # sort by num is close to 50
def myfunc(n):
 return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#copy a list
mylist = thislist.copy()
#join a list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 #1
for x in list2:
  list1.append(x) #2
  list1.extend(list2) #3

  #methods
#   append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# data types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))


tuple1 = (("parrot","sparrow"),("lion","tiger"))  # immutable (non changable)
print(tuple1)

dict1={"name":"yash","age":20} #maped data (dictionary)
print(dict1)

# operators

print(15//6) #floor division operator

print(5**3) #power
