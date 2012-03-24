from pprint import pprint

def merge(list0, list1):
    """Merge two sorted lists of numbers to produce a single sorted list of numbers.

    Arguments:
        list0 - First sorted list of numbers.
        list1 - Second sorted list of numbers.
    """
    newList = []
    index0, index1 = 0, 0
    len0, len1 = len(list0), len(list1)

    while ((index0 < len0) and (index1 < len1)):
        while ((index0 < len0) and (index1 < len1)) and (list0[index0] <= list1[index1]):
            newList.append(list0[index0])
            index0 = index0 + 1

        while ((index0 < len0) and (index1 < len1)) and (list1[index1] <= list0[index0]):
            newList.append(list1[index1])
            index1 = index1 + 1

    while index0 < len0:
        newList.append(list0[index0])
        index0 = index0 + 1

    while index1 < len1:
        newList.append(list1[index1])
        index1 = index1 + 1

    return newList

def mergeSort(list):
    """Sort the passed in list as per the standard merge sort algorithm

    Arguments:
        list - List of numbers
    """
    if len(list) == 0 or len(list) == 1:
        return list

    lstLen = len(list)
    mid = lstLen / 2

    list0, list1 = mergeSort(list[0:mid]), mergeSort(list[mid:lstLen])
    return merge(list0, list1)


import unittest
class TestMergeSort(unittest.TestCase):
    def testMergeEqualSize(self):
        self.assertEqual(merge([0, 5, 17], [3, 6, 20]), [0, 3, 5, 6, 17, 20])
        self.assertEqual(merge([0], [5]), [0, 5])
        self.assertEqual(merge([5], [0]), [0, 5])

    def testMergeUnequalSize(self):
        self.assertEqual(merge([0, 5], [3, 6, 20]), [0, 3, 5, 6, 20])
        self.assertEqual(merge([0, 5, 17], [3, 6]), [0, 3, 5, 6, 17])

    def testMergeBothEmpty(self):
        self.assertEqual(merge([], []), [])

    def testMergeOneEmpty(self):
        self.assertEqual(merge([], [0]), [0])
        self.assertEqual(merge([0], []), [0])
        self.assertEqual(merge([0, 5], []), [0, 5])
        self.assertEqual(merge([], [0, 5]), [0, 5])

    def testMergeSort(self):
        self.assertEqual(mergeSort([0, 5, 2, 10]), [0, 2, 5 ,10])
        self.assertEqual(mergeSort([]), [])
        self.assertEqual(mergeSort([1]), [1])
        self.assertEqual(mergeSort([100, 1000, 89]), [89, 100, 1000])

if __name__ == '__main__':
    unittest.main()
