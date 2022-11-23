## Data Abstraction - hides unnecessary code details from user

class Quote:
    # Hidden variable in Quote class
    # using double underscore/__ before attribute's name will not make them directly visible outside. 
    __prefix = "Hide Implementation"

    # method that modifies hidden variable
    def finish_quote(self, suffix):
        self.__prefix += " " + suffix
        print(self.__prefix)


quoteObject = Quote()
quoteObject.finish_quote("using abstraction.")

# Returns - AttributeError: 'Quote' object has no attribute '__prefix'
print(quoteObject.__prefix)
# hidden variables can be accessed outside a class with following usage
print(quoteObject._Quote__prefix)