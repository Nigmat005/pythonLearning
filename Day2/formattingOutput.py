# name="john";
# age=30
# sal=50000
name, age, sal = "john", 30, 50000.50
print("My name is: %s, age is:%d, salary is: %g" %(name,age,sal))
print("=======================================")
print("name is:", name, sep=" ")
print("age is:", age, sep=" ")
print("sal is:", sal, sep=" ")
print("=======================================")
print("His name is {0:<10}, thank you ".format(name))
print("His age is {0}".format(age))
print("His sal is {0}".format(sal))
print("=======================================")
print("My name is {name}".format(name=name))
print("My name is {age}".format(age=age))
print("My name is {salary}".format(salary=name))

print("=======================================")
print("My name is {0}, and age is {1},salary is {2}".format(name,age,sal))
print("=======================================")
print("My name is {name}, and age is {age},salary is {salary}".format(name=name,age=age,salary=sal))
print("=======================================")
print("My name is {0}, and age is {1},salary is {2}".format(name,age,sal))


