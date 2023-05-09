#sets
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

#Duplicates Not Allowed

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# add items to set
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# add sets
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# remove an item
thisset.discard("banana")

print(thisset)

# remove random item 
x = thisset.pop()

print(x)

print(thisset)

# clear set completely
thisset.clear()

print(thisset)

#delete set
del thisset

# join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
 
 #Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)