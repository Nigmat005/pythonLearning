def myFunc(a,b,c):
    print(a,b,c)
myFunc(10,20,30) # This is positional argument

myFunc(a=10,b=30,c=50)# This is keyWord argument

myFunc(10,b=40,c=80)# Both positional and argument

#myFunc(10,b=40,80)# Error bcoz positional argument MUST appear priori than keyWord argument