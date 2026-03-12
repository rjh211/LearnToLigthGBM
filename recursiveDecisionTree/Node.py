class Node:
    sourceList = []
    answer = []
    candidateList = []
    threshold = 0

    def __init__(self, sourceList, answer):
        self.sourceList = sourceList
        self.answer = answer
        self.candidateList = self.getCandidateList()

    def getCandidateList(self):
        return [(a + b) / 2 for (a, b) in zip(self.sourceList, self.sourceList[1:])]
        

    def calGiniValue(self, leftList, rightList):
        leftSize = len(leftList)
        rightSize = len(rightList)

        leftGini = 1 - (sum([(leftList.count(i) / leftSize) ** 2 for i in set(leftList)]))
        rightGini = 1 - (sum([(rightList.count(i) / rightSize) ** 2 for i in set(rightList)]))
        return (leftSize / len(self.sourceList)) * leftGini + (rightSize / len(self.sourceList)) * rightGini

    def findBestSplit(self):
        bestGini = float('inf')
        self.threshold = None
        for candidate in self.candidateList:
            LeftList = [self.answer[index] for index, value in enumerate(self.sourceList) if value <= candidate]
            RightList = [self.answer[index] for index, value in enumerate(self.sourceList) if value > candidate]
            giniValue = self.calGiniValue(LeftList, RightList)

            if giniValue < bestGini:
                bestGini = giniValue
                self.threshold = candidate


    def printResult(self, inputValue):
        self.findBestSplit()

        if inputValue <= self.threshold:
            print('go left')
        else:
            print('go right')