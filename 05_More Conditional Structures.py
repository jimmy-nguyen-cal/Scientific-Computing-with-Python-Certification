#--- Which will never print regardless of the value for x?

x = 3

if x <2:
    print('Below 2')
elif x >= 2:
    print('Two or More')
else:
    print('Something else')

#--- Try/Except Strcture
#--- if the code in the try works - the except is skipped
#--- if the code in the try fails -  it jumps to the except section

astr = 'Hello Bob'
try:
    istr = int(astr)
    print(istr)
except:
    ister = - 1
    print(ister)


#--- Second example
rawster = input('Enter a number: ')
try:
    ival = int(rawster)
except:
    ival = - 1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
