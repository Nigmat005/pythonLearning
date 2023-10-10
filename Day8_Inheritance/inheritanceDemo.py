# class A:
#     def m1(self):
#         print("This is m1 method from Parent")
#     @staticmethod
#     def staticMethod(var:str):
#         print("This is static method")
#         print("var is %s"%(var))
#
# class B(A):
#     def m2(self):
#         print("This is m2 method of child class ")



# objB=B();
# objB.m1()
# objB.m2()
# objB.staticMethod("Python")

globalvar1="This is global variable"

class A:
    def m1(self):
        print("This is m1 method of class A")

    @staticmethod
    def staticMethod(var: str):
        print("This is static method")
        print("var is %s" % (var))


class B():
    def m2(self):
        print("This is m2 method of class B ")


# Python allows multi inheritance--> one child can inherit from multi parent classes
# see example below
class C(A,B):
    globalvar1="This is globalVariable 2"
    def m3(self):
        print("This is m3 method of child class C ")
    def m2(self):
        print("this is m2 method from child class C")

objc=C();
print(objc.globalvar1)
# objc.m1()
# objc.m2()
# objc.m3()


class overload1:
    def printName(self):
        print("Hi this is Default")
    def printName(self,name=""):
        print("Hi this is "+name)

obj=overload1()
obj.printName("Nigmat")

