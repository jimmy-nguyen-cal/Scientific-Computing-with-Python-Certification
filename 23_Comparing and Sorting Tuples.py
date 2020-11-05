# --- sorting lists of tuples
d = {'a': 10,'b': 1,'c': 22}
print(d.items())

print(sorted(d.items()))

for k,v in sorted(d.items()):
    print(k,v)


# --- Sort by values instead of key
c = d
tmp = list()

for k, v in c.items():
    tmp.append((v,k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

# --- top 10 most common words
handle = open('mbox.txt')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, value in counts.items():
    newtup = (value,key)
    lst.append(newtup)
lst = sorted(lst, reverse= True)

for value, key, in lst[:10]:
    print(key, value)

# --- Even Shorter Version
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v,k) for k,v in c.items()], reverse= True))