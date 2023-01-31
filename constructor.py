class Person:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation

    # Each function in the class or the dunder methods take one argument must that is self is nothing but the object itself that has been passed automatically
    # Dunder methods that methods in python start with __ and ends with __ and also built in methods in python e.g, __init__ (constructor)
    def info(self):
        print(f"Name is {self.name} and it's occupation is {self.occupation}")

abhi = Person("abhishek","Software Developer")
harry = Person("harry","Software Engineer")
abhi.info()
harry.info()