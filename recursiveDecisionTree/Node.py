class Node:

    def __init__(self):
        self.sourceList = None
        self.answer = None
        self.candidateList = None
        self.threshold = None
        self.feature = None
        self.leftChild = None
        self.rightChild = None

    def setSourceList(self, sourceList):
        self.sourceList = self.featureTransfose(sourceList)
        self.candidateList = self.getCandidateList()

    def featureTransfose(self, sourceList):
        return [list(col) for col in zip(*sourceList)]
    
    def setAnswer(self, answer):
        self.answer = answer

    def getCandidateList(self):
        return [self.calCandidate(lst) for lst in self.sourceList]

    def calCandidate(self, source):
        return [(a + b) / 2 for (a, b) in zip(source, source[1:])]

    def calGiniValue(self, leftList, rightList):
        leftSize = len(leftList)
        rightSize = len(rightList)

        leftGini = 1 - (sum([(leftList.count(i) / leftSize) ** 2 for i in set(leftList)]))
        rightGini = 1 - (sum([(rightList.count(i) / rightSize) ** 2 for i in set(rightList)]))
        return (leftSize / (leftSize + rightSize)) * leftGini + (rightSize / (leftSize + rightSize)) * rightGini

    def findBestSplit(self):
        bestGini = float('inf')
        self.threshold = None
        for index, candidateList in enumerate(self.candidateList):
            for candidate in candidateList:
                LeftList = [self.answer[i] for i, value in enumerate(self.sourceList[index]) if value <= candidate]
                RightList = [self.answer[i] for i, value in enumerate(self.sourceList[index]) if value > candidate]
                giniValue = self.calGiniValue(LeftList, RightList)

                if giniValue < bestGini:
                    self.feature = index
                    bestGini = giniValue
                    self.threshold = candidate

    def buildTree(self, sourceList, answer):
        node = Node()

        node.setSourceList(sourceList)
        node.setAnswer(answer)
        
        if len(set(node.answer)) == 1 or node.threshold is None or node.feature is None:
            return node

        node.findBestSplit()

        node.leftChild = node.buildTree([sourceList[index] for index, value in enumerate(node.sourceList[node.feature]) if value <= node.threshold], [answer[index] for index, value in enumerate(node.sourceList[node.feature]) if value <= node.threshold])
        node.rightChild = node.buildTree([sourceList[index] for index, value in enumerate(node.sourceList[node.feature]) if value > node.threshold], [answer[index] for index, value in enumerate(node.sourceList[node.feature]) if value > node.threshold])

        return node


    def printResult(self, value):
        if self.leftChild is None and self.rightChild is None:
            return self.answer[0]
        if value[self.feature] <= self.threshold:
            return self.leftChild.printResult(value)
        else:
            return self.rightChild.printResult(value)