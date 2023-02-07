# note graph[0][0] = graph[row][column]
# graph 1 from page 105 in textbook
# graph 3 from page 109 in textbook
# graph 4 from https://www.tes.com/teaching-resource/dijkstra-practice-questions-solutions-6329821
# 0 represents nodes that cannot be reached


graph1 = [
    [0, 4, 3, 7, 0, 0, 0],
    [4, 0, 0, 1, 0, 5, 0],
    [3, 0, 0, 3, 5, 0, 0],
    [7, 1, 3, 0, 2, 2, 7],
    [0, 0, 5, 2, 0, 0, 2],
    [0, 5, 0, 2, 0, 0, 5],
    [0, 0, 0, 7, 2, 5, 0],
]
graph2 = [
    [0, 20, 30, 0, 0],
    [20, 0, 30, 0, 25],
    [30, 30, 0, 35, 0],
    [0, 0, 35, 0, 40],
    [0, 25, 0, 40, 0],
]
graph3 = [
    [0, 4, 2, 0, 0, 0, 0],
    [4, 0, 3, 7, 4, 0, 0],
    [2, 3, 0, 3, 0, 0, 0],
    [0, 7, 3, 0, 1, 2, 0],
    [0, 4, 0, 1, 0, 5, 7],
    [0, 0, 0, 2, 5, 0, 5],
    [0, 0, 0, 0, 7, 5, 0],

]
graph4 = [
    [0, 3, 4, 11, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 6, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 9, 0, 1, 0, 0, 0, 0],
    [11, 6, 9, 0, 5, 2, 16, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 10, 18, 0, 0],
    [0, 0, 1, 2, 0, 0, 19, 0, 3, 0],
    [0, 0, 0, 16, 10, 19, 0, 12, 7, 17],
    [0, 0, 0, 0, 18, 0, 12, 0, 0, 14],
    [0, 0, 0, 0, 0, 3, 7, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 17, 14, 8, 0]
]
lol = [
    [0,2,4,6,0,0,0,0,0],
    [2,0,1,0,0,4,0,0,0],
    [4,1,0,2,0,5,0,0,0],
    [6,0,2,0,4,0,1,0,0],
    [0,0,0,4,0,3,3,3,0],
    [0,4,5,0,3,0,0,6,0],
    [0,0,0,1,3,0,0,2,5],
    [0,0,0,0,3,6,2,0,2],
    [0,0,0,0,0,0,5,2,0]
]

examTest = [
    [0,12,13,0,15,0,0,0],
    [12,0,0,24,0,26,0,0],
    [13,0,0,34,0,0,37,0],
    [0,24,34,0,0,0,0,48],
    [15,0,0,0,0,56,57,0],
    [0,26,0,0,56,0,0,68],
    [0,0,37,0,57,0,0,78],
    [0,0,0,48,0,68,78,0]
]

allNodes = []
startNode = ''
endNode = ''


class Graph:
    def __init__(self):
        self.nodes = []
        self.matrix = examTest

    def add_node(self, label):
        self.nodes.append(label)

    def get_nodes(self):
        print(self.nodes)

    def get_adjacent_nodes(self, wantedNode):
        adjacentNodes = []
        visited = []
        repeat = False
        index = self.nodes.index(wantedNode)
        for connected in self.matrix[index]:
            if connected != 0:
                for i in visited:
                    if connected == i:
                        repeat = True
                if repeat:
                    start = self.matrix[index].index(visited[-1]) + 1
                    adjIndex = self.matrix[index].index(connected, start)
                elif not repeat:
                    adjIndex = self.matrix[index].index(connected)
                adjacentNodes.append(self.nodes[adjIndex])
                visited.append(connected)
            else:
                pass
        return adjacentNodes


class Nodes:
    def __init__(self, nodeLabel, workingVal, finalVal):
        allNodes.append(self)
        self.nodeLabel = nodeLabel
        self.workingVal = None
        self.finalVal = None

    def show(self):
        print('Working Val: ', self.workingVal, ' Final Val: ', self.finalVal)

    def fill_working_val(self):
        # for each adjacent node
        for adjacent in g.get_adjacent_nodes(self.nodeLabel):
            for n in allNodes:
                # identifying adjacent node
                if n.nodeLabel == adjacent:
                    # if the nodes final value is none
                    if n.finalVal is None:
                        if self.finalVal is None:
                            # find working value from the matrix without adding final val of current node
                            newWorkingVal = g.matrix[g.nodes.index(self.nodeLabel)][g.nodes.index(adjacent)]
                            # find working value from matrix adding the final value to it
                        else:
                            newWorkingVal = g.matrix[g.nodes.index(self.nodeLabel)][
                                                g.nodes.index(adjacent)] + self.finalVal

                        # if current adjacent node is none, then add the new working val
                        if n.workingVal is None:
                            n.workingVal = newWorkingVal
                        # or if the new working val is less than the current working val, then replace.
                        elif newWorkingVal <= n.workingVal:
                            n.workingVal = newWorkingVal

    def compare_working_val(self):
        tempAllWorkingVals = []
        for n in allNodes:
            if n.workingVal is not None and n.finalVal is None:
                tempAllWorkingVals.append(n.workingVal)
        smallest = min(tempAllWorkingVals)
        for n in allNodes:
            if n.workingVal == smallest and n.finalVal is None:
                nextNode = n
        nextNode.finalVal = smallest
        return nextNode

    def working_back(self):
        currentN = self
        pathOrder = [endNode]
        while currentN.nodeLabel != startNode:
            for adjacent in g.get_adjacent_nodes(currentN.nodeLabel):
                for n in allNodes:
                    if n.nodeLabel == adjacent:
                        path = g.matrix[allNodes.index(currentN)][allNodes.index(n)]
                        if path == 0:
                            pass
                        elif currentN.finalVal - path == n.finalVal:
                            pathOrder.insert(0, n.nodeLabel)
                            currentN = n

        print('The shortest path from', startNode, ' to ', endNode, 'is:\n', pathOrder)


g = Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_node('H')
g.add_node('I')
g.add_node('J')

nodeA = Nodes('A', None, None)
nodeB = Nodes('B', None, None)
nodeC = Nodes('C', None, None)
nodeD = Nodes('D', None, None)
nodeE = Nodes('E', None, None)
nodeF = Nodes('F', None, None)
nodeG = Nodes('G', None, None)
nodeH = Nodes('H', None, None)
nodeI = Nodes('I', None, None)
nodeJ = Nodes('J', None, None)

startNode = input('Enter Start Node: ')
endNode = input('Enter End Node: ')

for n in allNodes:
    if n.nodeLabel == startNode:
        currentNode = n
        n.finalVal = 0
    if n.nodeLabel == endNode:
        finalNode = n

while finalNode.finalVal is None:
    currentNode.fill_working_val()
    currentNode = Nodes.compare_working_val(currentNode)

Nodes.working_back(currentNode)

'''
•••Completed on 13/01/2021•••
'''
