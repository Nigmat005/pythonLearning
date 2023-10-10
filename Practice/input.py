# count, list = 0, []
# size = (int(input("Please enter the size of list")));
# print("The size of list is initiated as", size)
#
# while count < size:
#     # var = {print("Please Enter %d st number" % count) if count == 1 else {
#     #     print("Please Enter {count}nd number".format(count=count))} if count == 2
#     # else {print("Please Enter" + count + "rd nummber")} if count == 3
#     # else {"Please Enter {}th number".format(count)}}
#
#     # userInput = {(int(input("Entering:{}st number".format("1")))) if count==0 else (int (input("Entering:{}nd number".format("2"))))if count==1
#     #              else (int(input("Entering:{}rd number".format("3"))))if count==2 else (int (input("Entering:{}th number".format(count))))};
#
#     userInput = (int(input("Entering:{}st number".format("1"))) if count == 0 else (
#         input("Entering:{}nd number".format("2"))) if count == 1
#     else input("Entering:{}rd number".format("3")) if count == 2 else
#     input("Entering:{}th number".format(count)));
#     list.append(userInput)
#     print(type(userInput))
#     count += 1;
#
# print(list)


def userInput_List():
    count, list = 0, []
    size = (int(input("Please enter the size of list")));
    print("The size of list is initiated as", size)

    while count < size:
        userInput = (int(input("Entering:{}st number".format("1"))) if count == 0 else (
            input("Entering:{}nd number".format("2"))) if count == 1
        else input("Entering:{}rd number".format("3")) if count == 2 else
        input("Entering:{}th number".format(count)));
        list.append(userInput)
        count += 1;

    return list;


def evenAndodd(List):
    even, odd = 0, 0;
    for nums in List:
        if nums % 2 == 0:
            even += 1;
        else:
            odd += 1;
    return even, odd


even, odd = evenAndodd([1,2,3,4,5,6,7,8,9,10])
print("The count of even number in list is: {} The count of odd number in list is: {}".format(even,odd))
# print(type("Hi"))
# print(type({"Hi"}))
