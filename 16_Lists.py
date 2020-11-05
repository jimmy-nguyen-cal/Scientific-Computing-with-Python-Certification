# --- Lists and definite loops

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done')

# --- Looking inside lists
print(friends[2])


# --- How long is a list?
print(len(friends))

# --- Using the range function
print(range(len(friends)))

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)