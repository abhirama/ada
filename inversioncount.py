from pprint import pprint
#being sloppy here, using a global counter
inversionCount = 0

def mergeAndCount(list0, list1):
    """Merge two sorted lists of numbers to produce a single sorted list of numbers. Also, in the process counts a global counter of inversions seen so far.

    Arguments:
        list0 - First sorted list of numbers.
        list1 - Second sorted list of numbers.
    """
    newList = []
    index0, index1 = 0, 0
    len0, len1 = len(list0), len(list1)

    while ((index0 < len0) and (index1 < len1)):
        if list0[index0] <= list1[index1]:
            newList.append(list0[index0])
            index0 = index0 + 1
        else:
            newList.append(list1[index1])
            index1 = index1 + 1

            global inversionCount
            inversionCount = inversionCount + (len0 - index0)

    while index0 < len0:
        newList.append(list0[index0])
        index0 = index0 + 1

    while index1 < len1:
        newList.append(list1[index1])
        index1 = index1 + 1

    return newList

def countInversions(list):
    """Count the no of inversions in the passed in list.

    Arguments:
        list - List of numbers.
    """
    if len(list) == 0 or len(list) == 1:
        return list

    lstLen = len(list)
    mid = lstLen / 2

    list0, list1 = countInversions(list[0:mid]), countInversions(list[mid:lstLen])
    return mergeAndCount(list0, list1)

if False:
    fh = open('IntegerArray.txt')
    strInts = fh.readlines()

    ints = []
    for strInt in strInts:
        ints.append(int(strInt))

import unittest
class TestMergeSort(unittest.TestCase):
    def setUp(self):
        global inversionCount
        inversionCount = 0
        
    def test0(self):
        countInversions([5, 4, 3, 2, 1])
        self.assertEqual(inversionCount, 10)

    def test1(self):
        countInversions([])
        self.assertEqual(inversionCount, 0)

    def test3(self):
        countInversions([1, 1, 1])
        self.assertEqual(inversionCount, 0)

    def test4(self):
        countInversions([10, 6, 4, 2, 1, 11])
        self.assertEqual(inversionCount, (4 + 3 + 2 + 1))

    def test5(self):
        countInversions([1, 2, 3, 4, 5])
        self.assertEqual(inversionCount, 0)

if __name__ == '__main__':
    unittest.main()

