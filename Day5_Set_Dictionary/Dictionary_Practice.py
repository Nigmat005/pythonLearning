dic1={1:"Java",
      2:"Python",
      3:"C#",
      7:"swift",
      8:"HTML",
      9:"CSS",
      10:"SQL"}
# print(dic1)
#
# # get Value
# print(dic1[1])
#
# get all Key
for key in dic1:
    print(key)
#
# # get all Value
# for value in dic1.values():
#     print(value)
#
# # get both key and value
# for key, value in dic1.items():
#     print("key is: %s " %key,"value is:{} ".format(value))
#
# # add key and value in dictionary
#
# dic1[4]="Go"
# print(dic1)
#
# # use update
# dic1.update({5:"C",6:"JS"});
# print(dic1)
#




# print("Set Part=======================================")
# myset={1,2,3,4,5}
# myset.add(6)
# print(myset)
# # print(myset.remove(10)) #KeyError: 10
# print(myset.discard(10))
# print(myset.update({7,8,9,10}))
# print(myset)




#
test_dict = {'Gfg' : {'is' : 'best'}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# using nested get()
# Safe access nested dictionary key
res = test_dict.get('Gfg', {}).get('is')

print(test_dict.get("Gfg").get("is"))

# printing result
print("The nested safely accessed value is : " + str(res))