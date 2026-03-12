class Node:
    sourceList = None
    answer = None
    candidateList = None
    threshold = None
    feature = None
    leftChild = None
    rightChild = None

    def __init__(self):
        pass

    def setSourceList(self, sourceList):
        self.sourceList = sourceList
        self.candidateList = self.getCandidateList()
    
    def setAnswer(self, answer):
        self.answer = answer

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

    def buildTree(self, sourceList, answer):
        node = Node()

        node.setSourceList(sourceList)
        node.setAnswer(answer)
        
        if node.calGiniValue(answer, []) == 0:
            return node

        node.findBestSplit()

        node.leftChild = node.buildTree([value for value in sourceList if value <= node.threshold], [answer[index] for index, value in enumerate(sourceList) if value <= node.threshold])
        node.rightChild = node.buildTree([value for value in sourceList if value > node.threshold], [answer[index] for index, value in enumerate(sourceList) if value > node.threshold])

        return node


    def printResult(self, value):
        if self.leftChild is None and self.rightChild is None:
            return self.answer[0]
        if value <= self.threshold:
            return self.leftChild.printResult(value)
        else:
            return self.rightChild.printResult(value)