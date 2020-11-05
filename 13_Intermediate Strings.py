# --- Slicing Strings
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

# --- String Concatenation
a = 'Hello'
b = 'There'
c = a + ' ' + b
print(c)

# --- Using in as a logical Operator
fruit = 'banana'
var1 = 'n' in fruit
var2 = 'nan' in fruit
if 'a' in fruit:
    print('Found it!')

# --- String Library
greet = 'Hello Bob'
zap = greet.lower()
zap2 = greet.upper()
print(zap)
print(zap2)

greet = ' Hello Bob'
nstr = greet.replace('Bob', 'Jane').strip()
print(nstr)

# --- Prefixes
line = 'Please have a nice day'
print(line.startswith('Please'))

# --- Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
host = data[atpos:]
print(host)