import inversioncount

fh = open('IntegerArray.txt')
strInts = fh.readlines()

ints = []
for strInt in strInts:
    ints.append(int(strInt))

inversioncount.countInversions(ints)
print inversioncount.inversionCount
