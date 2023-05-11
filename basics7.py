# dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
x = thisdict.get("brand")
# x = thisdict.keys()  get all list of keys
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020
car["color"] = "red"
# thisdict.update({"year": 2020})
# thisdict.update({"color": "red"})
print(x) #after the change

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# remove element
#del thisdict["model"]
# thisdict.pop("model")
# del thisdict delete complete list
#thisdict.clear() clear list
#thisdict.popitem()  pop last item

# return values
for x in thisdict.values():
  print(x)

# returns keys
  for x in thisdict.keys():
  print(x)

# return items
for x, y in thisdict.items():
  print(x, y)

  # copy a list
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# nested 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


