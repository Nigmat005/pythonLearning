# import array
# vals=array.array('i',[5,9,8,4,2]);
# print(vals)

# import array as arr
# vals=arr.array('I',[5,9,-8,4,2]);
# print(vals.typecode)
# print(vals)


import array as arr
vals=arr.array('i',[5,9,-8,4,2]);
print(vals)
print(vals.buffer_info())  # return you Info of the array you working with. (2569385535184, 5)   (Address,Size)

print(vals.typecode)  # return i(means signed Integer) I(Unsigned Integer) ===>No negative

vals.reverse()
print(vals)

for i in range(len(vals)):
    print(vals[i])


# Working with char

charArray= arr.array('u',['a','b','c','d','e'])
print(charArray.typecode)
print(charArray)

# Copy one array to another when not knowing the type of array
# newArray=vals;
# print(newArray)

newArray=arr.array(vals.typecode,(a for a in vals));
print(newArray)