# from DemoPackage.demo1 import display
# display("John")

# from  DemoPackage.demo2 import greeting
# greeting().sayHi("Python")

# Using sys
import sys

sys.path.append("C:\\Users\\Nigma\\PycharmProjects\\pythonLearning\\Day9_Module\\DemoPackage")
import demo1
demo1.display("John")
import demo2
obj=demo2.greeting();
# demo2.greeting().sayHi("Jason")
obj.sayHi("Jason")

