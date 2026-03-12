from Node import Node

Node1 = Node()

RootNode = Node1.buildTree([3, 7, 11, 17], [1, 0, 1, 1])


for i in range(11):
    print('input value : '+ str(i) + ' result : ' + str(RootNode.printResult(i)))
