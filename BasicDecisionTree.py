sourceList = [3, 7, 11, 17]
answer = [0, 0, 1, 1]

def getCandidateList(sourceList):
    return [(a + b) / 2 for (a,b) in zip(sourceList, sourceList[1:])]

def calGiniValue(leftList, rightList):
    leftSize = len(leftList)
    rightSize = len(rightList)

    leftGini = 1 - (sum([(leftList.count(i) / leftSize) ** 2 for i in set(leftList)]))
    rightGini = 1 - (sum([(rightList.count(i) / rightSize) ** 2 for i in set(rightList)]))
    return (leftSize / len(sourceList)) * leftGini + (rightSize / len(sourceList)) * rightGini

def findBestSplit(candidateList):
    bestGini = float('inf')
    bestCandidate = None
    for candidate in candidateList:
        LeftList = [answer[index] for index, value in enumerate(sourceList) if value <= candidate]
        RightList = [answer[index] for index, value in enumerate(sourceList) if value > candidate]
        giniValue = calGiniValue(LeftList, RightList)

        if giniValue < bestGini:
            bestGini = giniValue
            bestCandidate = candidate

    return bestCandidate

def printResult(inputValue):
    bestCandidate = findBestSplit(getCandidateList(sourceList))

    if inputValue <= bestCandidate:
        print('go left')
    else:
        print('go right')


printResult(10)
