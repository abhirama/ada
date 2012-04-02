import random
import pprint

def quicksort(nos, startIndex, endIndex):
    if startIndex == endIndex:
        return nos
    else:
        pivotIndex = getPivotIndex(nos, startIndex, endIndex) 
        swap(nos, startIndex, pivotIndex)
        pivot = nos[startIndex]

        print "pivot is:", pivot

        pprint.pprint(foo)

        print "----------start----------"

        lesserThanPivotIndex = startIndex + 1

        for index in xrange(startIndex + 1, endIndex + 1):
            if nos[index] < pivot:
                swap(nos, lesserThanPivotIndex, index)
                lesserThanPivotIndex = lesserThanPivotIndex + 1

        print "----------end----------"

        pprint.pprint(foo)

        print "For swapping start index:{0}, end index:{1}".format(startIndex, lesserThanPivotIndex)
        swap(nos, startIndex, lesserThanPivotIndex - 1)

def getPivotIndex(nos, startIndex, endIndex):
    return random.randint(startIndex, endIndex)
    #return 3


def swap(nos, index0, index1):
    nos[index0], nos[index1] = nos[index1], nos[index0]


foo = [1, 2, 3, 4]
quicksort(foo, 0, len(foo) - 1)
pprint.pprint(foo)
