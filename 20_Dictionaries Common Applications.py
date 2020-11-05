#--- dictionary count

counts = dict()
names = ['csev', 'cwen','csev','zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


# --- get method
counts2 = {}
names = ['csev', 'cwen','csev','zqian', 'cwen']
for name in names:
    counts2[name] = counts2.get(name, 0) + 1
print(counts2)

