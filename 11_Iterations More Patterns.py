# --- Counting in a loop
print('\nCounting ...')
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74.15]:
    zork += 1
    print(zork, thing)
print('After', zork)

# --- Summing in a Loop
print('\nSumming...')
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork += thing
    print(zork, thing)
print('After', zork)

# --- Finding the average in a loop
print('\nAveraging ...')
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    sum += value
    print(count, sum, value)
print('After', count, sum, sum / count)

# --- Filtering in a loop
print('\nFiltering ...')
print('Before')
for value in [9, 41, 12, 3, 74.15]:
    if value > 20:
        print('Large number', value)
print('After')

# --- Search using a boolean variable
print('\nSearching ...')
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    else:
        found = False
    print(found, value)
print('After', found)

# --- Find the smallest value
print('\nSearching for the smallest value ...')
smallest_so_far = -1
print('Before', smallest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if num < smallest_so_far:
        smallest_so_far = num
    print(smallest_so_far, num)
print('After', smallest_so_far)

# --- How he would find the smallest number
# --- using the IS operator implies 'is the same as' and using None keyword
print('\nSearching for the smallest value ...')
smallest = None
print('Before', smallest)
for num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    print(smallest, num)
print('After', smallest)
