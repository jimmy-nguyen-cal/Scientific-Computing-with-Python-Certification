import re

# --- find() vs. re.search()
f = open('mbox.txt')
for line in f:
    line = line.rstrip()
    if line.find('Hello') >= 0:
        print(line)


# re.search()
f = open('mbox.txt')
for line in f:
    line = line.rstrip()
    if re.search('Hello', line):
        print(line)


# --- startswith vs. ^
f = open('mbox.txt')
for line in f:
    line = line.rstrip()
    if line.startswith('Hello'):
        print(line)

# --- ^ character
f = open('mbox.txt')
for line in f:
    line = line.rstrip()
    if re.search('^Hello', line):
        print(line)

# --- Matching and Extracting Data
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)


#--- Greedy Match vs Non. Greedy Match
x = 'From: Using the    : character'
y = re.findall('^F.+',x)
print(y)

# --- Non Greedy Match
y = re.findall('^F.+?:',x)
print(y)
