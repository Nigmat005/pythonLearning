# list=[1,2,3,4,5,6,7,8,9,10]
# for x in list:
#     print(x)
#
# for i in range(11):
#     print(i)

def printEven(num1,num2):
    for i in range(num1,num2):
        if i%2==0:
            print("Even Numbers Are: %d"%(i))



# printEven(1,11)


for i in range(1,21):
    if i%2!=0:
        continue
    else:
        print(i)
