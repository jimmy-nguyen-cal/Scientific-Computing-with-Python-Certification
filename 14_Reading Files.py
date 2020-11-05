
# --- Opening and reading the whole file
fhand = open('mbox.txt', 'r')
print(fhand.read())

# --- read one line of the file
f = open("mbox.txt", "r")
print('\n\t', f.readline())

# --- looping through the lines of the file, read the whole file, line by line

f = open("mbox.txt", "r")
for x in f:
  print(x)


# --- Opening and writing a file
f = open("mbox.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("mbox.txt", "r")
print(f.read())