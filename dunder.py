class Dog:
    def __init__(self, name):
        self.name = name
        self.good_dog = True
    
    def __str__(self):
        return self.name


maddie = Dog('Maddie')
print(str(maddie))
print(maddie)

''' Other useful dunder methods include...
-----------------------------------------------------------
__getattr__ for when you get an attribute (i.e. maddie.name)
__setattr__ for when you get an attribute (i.e. maddie.name = 'Madison')
__len__ for when you call len on the class
__add__ for when you add instances of the class
__getitem__ for using bracket notation on an instance of the class (i.e. maddie['food'])
----------------------------------------------------------------------------------------
'''