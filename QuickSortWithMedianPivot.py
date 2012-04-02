from quicksort import QuickSort

class QuickSortWithMedianPivot(QuickSort):
    #will not work in case of duplicates, must be possible to do this more efficiently without using lists
    def getPivotIndex(self, nos, startIndex, endIndex):
        middleIndex = startIndex + ((endIndex - startIndex) / 2)
        listForMedian = [nos[startIndex], nos[middleIndex], nos[endIndex]]
        maxElem = max(listForMedian)
        listForMedian.remove(maxElem)
        maxElem = max(listForMedian)
        return nos.index(maxElem)

import unittest
class TestQuickSort(unittest.TestCase):
    def test(self):
        quickSort = QuickSortWithMedianPivot()

        if True:
            self.assertEqual(quickSort.sort([0, 5, 17]), [0, 5, 17])
            print "Comparision count is:", quickSort.getComparisionCount()
            self.assertEqual(quickSort.sort([]), [])
            print "Comparision count is:", quickSort.getComparisionCount()

        self.assertEqual(quickSort.sort([5, 4, 3, 2, 1, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        print "Comparision count is:", quickSort.getComparisionCount()

if __name__ == '__main__':
    unittest.main()
