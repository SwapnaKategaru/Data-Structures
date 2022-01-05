# Inheritance helps inherit or access properties from one to another class
# Maintains relationship betweeen classes and hence provides CODE REUSABILITY
# Every subclass has accesss to all properties inherited from its superclass
# If subclass 'B' is inherited from 'A', then all subclasses of 'B' also inherit from 'A'.


# Super-class or Base-class or Parent-class
# object class is ROOT of all classes and is inherited to all classes
class Country(object):
    def __init__(self, place):
        self.place = place
    
    def get_place(self):
        return self.place

    def add_country(self, new_country):
        self.place = new_country
        return self.place

    def is_state(self):
        return False

# Sub-class or Inherited-class or Child-class
# class subclass_name(superclass_name): 
class State(Country):                            # child-class (State) defining it's parent-class as (Country)
    def is_state(self):
        return True


country = Country('India')
country.add_country('Japan')
country.get_place()

state = State('Karnataka')

print(country.get_place(), country.is_state())
print(state.get_place(), state.is_state())

print(Country.is_state('Carolina'))
print(State.is_state('Carolina'))