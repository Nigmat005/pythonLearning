myTuple=("Apple","Banana","cherry");
print(myTuple)

# Example2: access tuple items

print(myTuple[1])
print(myTuple[-1])

# myTuple=("Apple","Banana","cherry","orange","kiwi","melon","mango");
# print(myTuple[2:5])
# print(myTuple[2::2])
# print(myTuple[:])
# print(myTuple[::1])
# print(myTuple[5::-1])
# print(myTuple[-5:-1:1])
# print(myTuple[-5::1])
# print(myTuple[::-1])
# print(myTuple[-1:-5:-1])

# Create tuple with one element
var1="Hello";
print(type(var1))

del (var1)
var1=("hello");
print(type(var1))

var2=("hello",)
print(type(var2))

#Example 4: Change tuple items
#by default tuple does not allow you change value bcoz it is immutable
#tuple-->list(modify)--->tuple
#
# myTuple=("Apple","Banana","cherry");
# mylist=list(myTuple);
# print(type(mylist))
# mylist[0]="Orange"
#
# myTuple=tuple(mylist)
# print(myTuple)

#Example check if item in Tuple
myTuple=("Apple","Banana","cherry");
# myTuple2=tuple(list(myTuple).copy())
myTuple2=myTuple;

{print("yes")}if "Banana" in myTuple else {print("no")}

print(myTuple)
print(len(myTuple2))