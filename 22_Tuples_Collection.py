# --- Tuples are like lists

x= ('Glenn', ' Sally', 'Joseph')
print(x[2])

y= (1,9,2)
print(y)
print(max(y))


# --- Tuples and Assignment
(x,y) = (4,'fred')
print(y)

(a,b) = (99,98)
print(a)

# ---  Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)