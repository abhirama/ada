from quicksort import QuickSort

class QuickSortWithFirstElementPivot(QuickSort):
    def getPivotIndex(self, nos, startIndex, endIndex):
        return startIndex

import unittest
class TestQuickSort(unittest.TestCase):
    def test(self):
        quickSort = QuickSortWithFirstElementPivot()

        self.assertEqual(quickSort.sort([0, 5, 17]), [0, 5, 17])
        print "Comparision count is:", quickSort.getComparisionCount()

        self.assertEqual(quickSort.sort([]), [])
        print "Comparision count is:", quickSort.getComparisionCount()

        self.assertEqual(quickSort.sort([5, 4]), [4, 5])
        print "Comparision count is:", quickSort.getComparisionCount()

        self.assertEqual(quickSort.sort([5, 4, 3]), [3, 4, 5])
        print "Comparision count is:", quickSort.getComparisionCount()

        print "Comparision count is:", quickSort.getComparisionCount()
        self.assertEqual(quickSort.sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
