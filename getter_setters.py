class MainClass:
    def __init__(self,value):
        self._value = value
    
    # You can use @property decorator to make the function as a getter you can access the value function as an property of an object
    @property
    def value(self):
        return self._value*2
    
abhi = MainClass(8)
print(abhi.value)
