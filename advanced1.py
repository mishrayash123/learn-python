# open file
# f = open("demofile.txt", "rt")

# read file
# print(f.read())
# read only one line
# print(f.readline())

# read only parts of file
# print(f.read(5))

# using for loop
# for x in f:
#   print(x)

# close the file
# f.close()

# write in existing
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

#open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())

# create a new file
# f = open("myfile.txt", "x")

# delete  a file
import os
if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")