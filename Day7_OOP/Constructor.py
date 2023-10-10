

a="Hello"
b="Python"
class ConstructorPractice():
    a,b="",""

    # c: str="Good";
    # d: int="Good";

    def __init__(self,var1,var2):
        self.var1=var1;
        self.var2=var2;
    def instanceMethod(self,a:str,b:str):
        self.a=a; self.b=b;
        print("This is instance method")
        print("result is: %s  %s" %(self.a,self.b))
        print("var1 is {0} and var2 is {1}".format(self.var1,self.var2))

    @staticmethod
    def staticMethod(self):
        print("This static method")
        print("This is the Value of 'Self' KeyWord:{0}".format(self))

    def staticMethod2(self,a,b):
        '''
        A static method doesn’t have access to the class and instance variables because it does not receive an implicit first argument like self and cls. Therefore it cannot modify the state of the object or class.
        '''
        print("This is static method2")
        print("The result is : {a}  {b}".format(a=a,b=b))

    def callGlobal(self):
        print("Calling Global Method")
        print("result is: %s  %s" % (a, b))


obj1=ConstructorPractice("Akag","Xax");
obj1.instanceMethod("Hello","Java")
# obj1.callGlobal()

# Calling Static Method
# ConstructorPractice.staticMethod("Happy Learning")
# ConstructorPractice.staticMethod2("","Hello","C#")
