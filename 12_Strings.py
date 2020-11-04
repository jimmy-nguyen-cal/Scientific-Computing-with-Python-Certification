# --- String Data type

str1 = 'Hello'
str2 = ' there'
bob = str1 + str2
print(bob)


# --- Reading and Converting
apple = input('Enter:')
x = int(apple) - 10
print(x)

# --- Looking Inside Strings
fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

# --- Len Function
fruit = 'banana'
x = len(fruit)
print(x)

# --- Looping through strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

fruit = 'banana'
for letter in fruit:
    print(letter)

# --- Looping and Counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)