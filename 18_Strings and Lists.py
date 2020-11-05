# --- split() function as splitting words

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

# --- the double split pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan     5 09:14:16 2008'
words = line.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)
