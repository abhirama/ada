import pprint

class QuickSort:
    def sort(self, nos):
        self.comparisionCount = 0
        return self.quickSortHelper(nos, 0, len(nos) - 1)

    def quickSortHelper(self, nos, startIndex, endIndex):
        if endIndex - startIndex <= 0:
            return nos
        else:
            #print "End index:{0}, Start index:{1}".format(endIndex, startIndex)
            self.comparisionCount = self.comparisionCount + (endIndex - startIndex)
            pivotIndex = self.getPivotIndex(nos, startIndex, endIndex) 
            #print "Pivot index is:", pivotIndex
            self.swap(nos, startIndex, pivotIndex)
            pivot = nos[startIndex]

            lesserThanPivotIndex = startIndex + 1

            for index in xrange(startIndex + 1, endIndex + 1):
                if nos[index] < pivot:
                    self.swap(nos, lesserThanPivotIndex, index)
                    lesserThanPivotIndex = lesserThanPivotIndex + 1

            self.swap(nos, startIndex, lesserThanPivotIndex - 1)
            #pprint.pprint(nos)
            #print ""

            self.quickSortHelper(nos, startIndex, lesserThanPivotIndex - 2)
            self.quickSortHelper(nos, lesserThanPivotIndex, endIndex)
        return nos

    def getPivotIndex(self, nos, startIndex, endIndex):
        pass

    def swap(self, nos, index0, index1):
        nos[index0], nos[index1] = nos[index1], nos[index0]

    def getComparisionCount(self):
        return self.comparisionCount
