# --- concatenating lists
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)


# --- Lists can be sliced using :
print(c[1:3])
print(c[:])


# --- Building a list from Scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)


# --- is something in a list
print(9 in c)



# --- User input and lists
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print('Average:', average)