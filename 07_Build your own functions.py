# --- Arguements

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


greet('en')


# --- Return Values
def greet():
    return "Hello"


print(greet(), "Glenn")


# --- Rewritten with return as a real function
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'), 'Glenn')


# --- Multiple Parameters / Arguments
def addtow(a, b):
    added = a + b
    return added

x = addtow(3,5)
print(x)
