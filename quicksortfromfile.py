from QuickSortWithLastElementPivot import QuickSortWithLastElementPivot 
from QuickSortWithFirstElementPivot import QuickSortWithFirstElementPivot
from QuickSortWithMedianPivot import QuickSortWithMedianPivot

fh = open('QuickSort.txt')
strInts = fh.readlines()

ints = []
for strInt in strInts:
    ints.append(int(strInt))

quickSortWithFirstElementPivot = QuickSortWithFirstElementPivot()
quickSortWithFirstElementPivot.sort(list(ints))
print "First element pivot:", quickSortWithFirstElementPivot.getComparisionCount()

quickSortWithMedianPivot = QuickSortWithMedianPivot()
quickSortWithMedianPivot.sort(list(ints))
print "Median element pivot:", quickSortWithMedianPivot.getComparisionCount()

quickSortWithLastElementPivot = QuickSortWithLastElementPivot()
quickSortWithLastElementPivot.sort(list(ints))
print "Last element pivot:", quickSortWithLastElementPivot.getComparisionCount()


