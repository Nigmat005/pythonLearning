import keyword

myList=["Apple","Banana","cheery"];
for fruit in myList:
   print(fruit)

{print("cheery is in the list")} if "cheery" in myList else{print("cheery is not in the list")}


# List Length
print(len(myList))
print(len(myList[0]));

# add new item in list
myList.append("Strawberry")
print(myList)

myList.insert(6,"Strawberry")
myList.insert(2,"Strawberry")
print(myList)

# remove item from list
myList.remove("Strawberry") # remove first occurrence of existing element
print(myList)

myList.pop(3)  # remove occurrence of existing element by index
print(myList)

# deleting by 'del' keyword
del myList[2]
print(myList)

# clear function
myList.clear();  # remove all items
print(myList)

# reverse item from list
myList.reverse();
print(myList)

# print all keyword in Python
print(keyword.kwlist)

# copy one list to another list
#  use list() function
myList1=["Apple","Banana","cheery"]
myList2=list(myList1)
print(myList2)

# use copy function
myList2=myList1.copy();
print(myList2)

# use extend function
print("Using extend function======================================")
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list1.extend(list2)
print(list1)

# join two lists
continentList=["Asia","NorthAmerica","Europe","Africa","South America"]
contryList=["Japan","US","Germany","South Africa","Argentina"]
locationList=[];
# locationList=continentList+contryList;
# print(locationList)

# i=0;
# for continents in continentList:
#    locationList.append(continents)
#    while(i<len(contryList)):
#       locationList.append(contryList[i])
#       i+=1;
#       break;
#
#
# print(locationList)
# print("===================test======================================")
# locationList.insert(3,"Python")
# print(locationList)

i=0; j=1;
for continents in continentList:
   locationList.append(continents)
   while(i<len(contryList)):
      locationList.insert(j,contryList[i])
      i+=1;
      j+=2;
      break;


print(locationList)


print("===============================removeAllDigits================================")
num=["1","2","3","4","5"]
String=["a","b","c","d","e"]
combinedList=num+String

i=0;
for x in combinedList[:]:
   if x.isdigit():
      combinedList.pop(combinedList.index(x));

print("After removing all digits: ",combinedList)


# combinedList.extend(str)
# combinedList.extend(num)
print("Before removing digits",combinedList,sep=" ")
print("the length of list is: {}".format(len(combinedList)));
combinedList.pop(0)
print("After remove the 1 ",combinedList)
print("After remove one element,the length of list is: {}".format(len(combinedList)));






# for x in combinedList[:]:
#    if(x.isnumeric()):
#       combinedList.remove(x)
#    i=i+1;
#
# print(combinedList)