import random
import pprint

class QuickSort:
    def sort(self, nos):
        return self.quickSortHelper(nos, 0, len(nos) - 1)

    def quickSortHelper(self, nos, startIndex, endIndex):
        if startIndex == endIndex or startIndex > endIndex:
            return nos
        else:
            pivotIndex = self.getPivotIndex(nos, startIndex, endIndex) 
            self.swap(nos, startIndex, pivotIndex)
            pivot = nos[startIndex]

            lesserThanPivotIndex = startIndex + 1

            for index in xrange(startIndex + 1, endIndex + 1):
                if nos[index] < pivot:
                    self.swap(nos, lesserThanPivotIndex, index)
                    lesserThanPivotIndex = lesserThanPivotIndex + 1

            self.swap(nos, startIndex, lesserThanPivotIndex - 1)

            self.quickSortHelper(nos, startIndex, lesserThanPivotIndex - 2)
            self.quickSortHelper(nos, lesserThanPivotIndex, endIndex)
        return nos

    def getPivotIndex(self, nos, startIndex, endIndex):
        return random.randint(startIndex, endIndex)

    def swap(self, nos, index0, index1):
        nos[index0], nos[index1] = nos[index1], nos[index0]

import unittest
class TestQuickSort(unittest.TestCase):
    def test(self):
        quickSort = QuickSort()
        self.assertEqual(quickSort.sort([0, 5, 17]), [0, 5, 17])
        self.assertEqual(quickSort.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(quickSort.sort([]), [])

if __name__ == '__main__':
    unittest.main()
