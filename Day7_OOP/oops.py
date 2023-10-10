#Example1:
# Java ---->OOP
# Python -----> Structure + OOP
class MyClass:
    def myMethod(self):
        pass
    def disPlay(self,name,greetMSG):
        print("Here we running \"display\" method, 'name' is %s and 'message' is %s "%(name,greetMSG))
        print("Method is running: taking parameter name as {name}, greetMSG as {greetMSG} ".format(name=name,greetMSG=greetMSG))
obj1=MyClass();
obj1.disPlay("John","How are you bro")

