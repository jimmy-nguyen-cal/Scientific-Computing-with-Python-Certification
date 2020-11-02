# --- Repeated Steps

n = 5
while n > 0:
    print(n)
    n = n - 1

print('Blastoff!')
print(n)


#--- Infinite Loop
n = 5
#while n > 0:
    #print('Leather')
    #print('Rinse')
print('Dry off!')

# --- Breaking out of a loop
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

#--- Finishing an iteration with continue
# continue statement ends the current iteration and jumps to the top of the loop and
# starts the next iteration
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')