# Encapsulation helps create restrictions or to avoid access of either variables/functions between classes
# Members of class that cannot be accessed are Private/Protected members
# Variables can be made private by using '__' as prefix to it's name

class Developers:
    def __init__(self):
        self.database = "PostgreSQL"
        self.__password = "It's private"          # Private member (variable)
        print("Password is only accessible to Developers: ", self.__password)

class Interns(Developers):
    def __init__(self):
        Developers.__init__(self)                 # Call to parent-class constructor
        print("Private member of super-class is called: ", self.__password)         # private members are not accessible by other class & returns error


dev_class = Developers()
print(dev_class.database)
#print(dev_class.__password)                      # Returns AttributeError as private member can't be accessed outside class

intern_class = Interns()
print(intern_class.database)