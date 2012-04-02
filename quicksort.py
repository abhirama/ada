import random
import pprint

def quickSort(nos):
    return quickSortHelper(nos, 0, len(nos) - 1)

def quickSortHelper(nos, startIndex, endIndex):
    if startIndex == endIndex or startIndex > endIndex:
        return nos
    else:
        pivotIndex = getPivotIndex(nos, startIndex, endIndex) 
        swap(nos, startIndex, pivotIndex)
        pivot = nos[startIndex]

        lesserThanPivotIndex = startIndex + 1

        for index in xrange(startIndex + 1, endIndex + 1):
            if nos[index] < pivot:
                swap(nos, lesserThanPivotIndex, index)
                lesserThanPivotIndex = lesserThanPivotIndex + 1

        swap(nos, startIndex, lesserThanPivotIndex - 1)

        quickSortHelper(nos, startIndex, lesserThanPivotIndex - 2)
        quickSortHelper(nos, lesserThanPivotIndex, endIndex)
    return nos

def getPivotIndex(nos, startIndex, endIndex):
    return random.randint(startIndex, endIndex)
    #return 3

def swap(nos, index0, index1):
    nos[index0], nos[index1] = nos[index1], nos[index0]

import unittest
class TestQuickSort(unittest.TestCase):
    def test(self):
        self.assertEqual(quickSort([0, 5, 17]), [0, 5, 17])
        self.assertEqual(quickSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quickSort([]), [])

if __name__ == '__main__':
    unittest.main()
