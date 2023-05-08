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
