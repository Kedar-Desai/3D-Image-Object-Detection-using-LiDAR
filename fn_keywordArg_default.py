def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName+',' + firstName)
    else:
        print(firstName, lastName)


# Default values allow a programmer to call a
def printName(firstName, lastName, reverse=False):
    if reverse:
        print(lastName+','+firstName)
    else:
        print(firstName, lastName)


printName('Kedar', 'Desai', True)  # Positional argument
printName(lastName='Desai ', firstName='Kedar', reverse=False)
# It is not legal to follow a keyword argument with a non-keyword argument e.g. printName(lastName)
printName('Kedar', 'Desai')   # Positional with default values
printName('Kedar', 'Desai', reverse=True)  # Default values allow
