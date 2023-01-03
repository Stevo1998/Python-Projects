# Defining a class with a protected variable 
class Encapsulated:
    def __init__(self):
        self._protectedVar = '20' # Set 19 to be protected by using a single underscore as the prefix.
        self.__privateVar = '23' # Set 98 to be private by using two inderscores as the prefix.

    # Definingt an atrribute in which both variables are printed
    def getEncapsulated(self): 
        print(self._protectedVar + self.__privateVar)


obj = Encapsulated() # Creating an object called obj and  set the value equal to the defined Encapsulated class
obj.getEncapsulated() # Using obj to print print both variables

    
