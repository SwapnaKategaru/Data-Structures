# Polymorphism helps create a function of various forms/functionality
# Polymorphism in different examples

# In-built functions that show polymorphism
print("Same function 'len' performs count on two different types(polymorphism)")
print('Length function counts len of string : ', len('This is a string'))
print('Length function counts len of list as well : ', len(['This', 'is', 'a', 'list']))
print('\n')

# Polymorphism using object and classes
class Java:
    def type(self):
        print("Java is a statically typed and compiled language")
    
    def performance(self):
        print("Faster Runtime")

    def founder(self):
        print("Java is introduced by James Gosling")


class Python:
    def type(self):
        print("Python is a dynamically typed and interpreted language")
    
    def performance(self):
        print("Runtime is slower compared to java")

    def founder(self):
        print("Python is introduced by Guido van Rossum")


object_java = Java()
object_python = Python()

for language in (object_java, object_python):
    language.founder()
    language.type()
    language.performance()



# Polymorphism using Inheritance
class Space:
    def galaxy(self):
        print("Milky Way is our galaxy")

    def existence(self):
        print("All the planets in solar system do not support life existence")

class Earth(Space):
    def existence(self):
        print("Earth supports existence of life")

class Others(Space):
    def existence(self):
        print("Life on other planets is uncertain")


object_space = Space()
object_earth = Earth()
object_neighbor_planets = Others()

print("\n")

object_space.galaxy()
object_space.existence()

object_earth.galaxy()
object_earth.existence()

object_neighbor_planets.galaxy()
object_neighbor_planets.existence()

print('\n')

# Polymorphism in function
def multiply(a, b=1):
    result = a * b
    return result

print(multiply(3))
print(multiply(3,2))