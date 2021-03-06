# --- Counting Pattern

counts = dict()
print('Enter a line of text:   ')
line = input('')

words = line.split()
print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


# list of keys
print(list(counts))
print(counts.keys())

# list of values
print(counts.values())

# list of items
print(counts.items())

# --- Definite Loops and Dictionaries
counts = {'chuck':1, 'fred': 42, 'jan': 100}
for key, value in counts.items():
    print(key, value)

# --- mini program

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)