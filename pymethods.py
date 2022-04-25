# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
    #Dunder Init Method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Methods: 
    """# Instance methods are the most common type of methods in Python classes. 
         These are so called because they can access unique data of their instance.
       # Instance methods must have self as a parameter, but you don't need to 
         pass this in every time. Self is another Python special term. Inside 
         any instance method, you can use self to access any data or methods 
         that may reside in your class. You won't be able to access them without
         going through self.
       # Finally, as instance methods are the most common, there's no decorator
         needed. Any method you create will automatically be created as an instance 
         method, unless you tell Python otherwise.
    
    """
    def example_function(self):
        """ This method is an instance method! """
        print('I\'m an instance method!')
        print('My name is ' + self.name)
	
	# a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
	
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
	    return age > 18

person1 = Person('Brook', 4)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.example_function())
print (person1.age)
print (person2.age)

# print the result
print (Person.isAdult(22))


class DecoratorExample:
  """ Example Class """
  def __init__(self):
    """ Example Setup """
    print('Dunder: Hello, World!')

  @staticmethod
  def example_function():
    """ This method is decorated! """
    print('I\'m a decorated function!')
 
de = DecoratorExample()
de.example_function()

"""
PS C:\Users\fitwialem\Documents\GitHub> python pymethods.py
I'm an instance method!
My name is Brook       
None
4
26
True
Dunder: Hello, World!
I'm a decorated function!
PS C:\Users\fitwialem\Documents\GitHub>
"""