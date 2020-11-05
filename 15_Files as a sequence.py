# --- File Handle as a sequence

xfile = open('mbox.txt')
for line in xfile:
    print(line)

# --- Counting lines in a file
f = open("mbox.txt")
count = 0
for line in f:
    count += 1
print('Line count:', count)

# --- Reading the whole file
f = open('mbox.txt')
inp = f.read()
print(len(inp))
print(inp[:20])

# --- Searching Through a file
f = open('mbox.txt')
for line in f:
    # line = line.rstrip() # removing white spaces if needed
    if line.startswith('Hello'):
        print(line)

# --- Skipping with continue
# --- we can convieniently skip a line by using the continue statement
f = open('mbox.txt')
for line in f:
    # line = line.rstrip() # removing white spaces if needed
    if not line.startswith('Hello'):  # if line does not start with hello, continue
        continue
    print(line)

# --- Using the in operator to select lines
f = open('mbox.txt')
for line in f:
    # line = line.rstrip() # removing white spaces if needed
    if not 'Hello' in line:  # if line does not start with hello, continue
        continue
    print(line)

# --- Prompt for file name
fname = input('Enter the file name:    ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
for line in fhand:
    # line = line.rstrip() # removing white spaces if needed
    if not 'Hello' in line:  # if line does not start with hello, continue
        continue
    print(line)
