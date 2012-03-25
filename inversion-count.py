#being sloppy here, using a global counter
inversionCount = 0

def mergeAndCount(list0, list1):
    """Merge two sorted lists of numbers to produce a single sorted list of numbers. Also, as a side effect count the no of inversions.

    Arguments:
        list0 - First sorted list of numbers.
        list1 - Second sorted list of numbers.
    """
    newList = []
    index0, index1 = 0, 0
    len0, len1 = len(list0), len(list1)

    alreadyCounted = False

    while ((index0 < len0) and (index1 < len1)):
        while ((index0 < len0) and (index1 < len1)) and (list0[index0] <= list1[index1]):
            newList.append(list0[index0])
            index0 = index0 + 1

        while ((index0 < len0) and (index1 < len1)) and (list1[index1] <= list0[index0]):
            if ((list1[index1] != list0[index0]) and (not alreadyCounted)):
                global inversionCount
                inversionCount = inversionCount + (len1 - index1)
                alreadyCounted = True
            newList.append(list1[index1])
            index1 = index1 + 1

    while index0 < len0:
        newList.append(list0[index0])
        index0 = index0 + 1

    while index1 < len1:
        newList.append(list1[index1])
        index1 = index1 + 1

    return newList

def countInversions(list):
    """Count the no of inversions in the passed in list

    Arguments:
        list - List of numbers.
    """
    if len(list) == 0 or len(list) == 1:
        return list

    lstLen = len(list)
    mid = lstLen / 2

    list0, list1 = countInversions(list[0:mid]), countInversions(list[mid:lstLen])
    return mergeAndCount(list0, list1)

countInversions([10, 1, 1, 2, 4, 3, 1])
print inversionCount

