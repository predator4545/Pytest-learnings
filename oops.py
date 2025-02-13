class parent:
    mark = None    #this is a class variable since this is a declared under a class
    def __init__(self,name,age):
        self.name = name       #assigning name value to self.name(means object.name), so it can be used around
        self.age = age
    def printa(self,ID):
        print("vankam  "+ID)
        print(self.mark)   #parent.mark will also work

class child(parent):
    def type(self):
        print(self.name)   #can't use parent.name
        self.printa("34ddsd")    ##can't use parent.printa
        print(parent.mark)

c1 = child("bala",3)

c1.type()


#self:  is representing the calling object  eg..   <__main__.child object at 0x00000239995DFB60>

#Class variables in object-oriented programming can be accessed using both the class name and an object reference because they are shared among all instances of the class. Let’s break this down in detail:

#1. Class Variables Are Shared
#Class variables are defined at the class level, outside of any instance methods. They belong to the class itself, rather than any particular instance.
#All objects of the class share the same copy of the class variable.

#Using the class name is the most explicit and preferred way to refer to class variables, as it makes it clear that the variable belongs to the class, not an instance.


#3. Access via Object Reference
#An object reference can also access class variables because the object first checks if the variable exists in its own instance namespace. If it doesn’t, it checks in the class namespace.

#If you assign a value to a class variable using an object reference, Python creates an instance variable in the object's namespace, leaving the original class variable unaffected

class Example:
    class_var = 10  # Class variable

# Accessing via class name
print(Example.class_var)  # Output: 10

# Accessing via object reference
obj1 = Example()
print(obj1.class_var)  # Output: 10


obj1 = Example()
obj1.class_var = 30  # Creates an instance variable

print(obj1.class_var)    # Output: 30 (instance variable)
print(Example.class_var) # Output: 10 (unchanged class variable)

#5. Why Allow Both?
#Allowing access to class variables through both the class and an object reference provides flexibility:

#Via Class Name: For clarity and when you want to ensure you're working with the class variable.
#Via Object Reference: For convenience, particularly when you don't know or care if the variable is defined at the instance or class level.
#However, modifying class variables through object references can lead to confusion and unintended behavior. It’s generally better to use the class name for clarity when dealing with class variables.
...