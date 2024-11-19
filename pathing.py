import graph_data as graph_data_file
import global_game_data
from numpy import random
import sys
import heapq as heap
import math


#graph_data[a] = gives you graph at index a
#graph_data[a][0] = start node of graph a
#graph_data[a][length-1] = exit node of graph a
#graph_data[a][b][0] = x-y coordinates as tuple of point b in graph a
#graph_data[a][b][1] = adjacency list of point b in graph a


def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data_file.test_path[global_game_data.current_graph_index]


def get_random_path():
    assert (global_game_data.current_graph_index is not None), "Current graph index cannot be None."
    assert (graph_data_file.graph_data is not None), "Graph_data cannot be None."
    graphIndex = global_game_data.current_graph_index
    assert (graph_data_file.graph_data[global_game_data.current_graph_index] is not None), "Graph_data at graph index cannot be None."
    graph = graph_data_file.graph_data[graphIndex]
    lastIndex = 0
    currentIndex = 0
    nextIndex = -1

    targetIndex = global_game_data.target_node[graphIndex]
    endIndex = len(graph) - 1

    reachedTarget = False
    reachedEnd = False

    path = list()
    while(not reachedTarget and not reachedEnd):
        while(not reachedTarget):
            if(currentIndex == targetIndex):
                reachedTarget = True
            else:
                numberOfAdjacentSpaces = len(graph[currentIndex][1])

                nextIndex = graph[currentIndex][1][random.randint(0, numberOfAdjacentSpaces)]

                if(numberOfAdjacentSpaces != 1):
                    while(lastIndex == nextIndex or currentIndex == nextIndex):
                        nextIndex = graph[currentIndex][1][random.randint(0, numberOfAdjacentSpaces)]
                
                lastIndex = currentIndex
                currentIndex = nextIndex
                path.append(currentIndex)

        while(not reachedEnd):
            if(currentIndex == endIndex):
                reachedEnd = True
            else:
                numberOfAdjacentSpaces = len(graph[currentIndex][1])

                nextIndex = graph[currentIndex][1][random.randint(0, numberOfAdjacentSpaces)]

                if(numberOfAdjacentSpaces != 1):
                    while(lastIndex == nextIndex or currentIndex == nextIndex):
                        nextIndex = graph[currentIndex][1][random.randint(0, numberOfAdjacentSpaces)]
                
                lastIndex = currentIndex
                currentIndex = nextIndex
                path.append(currentIndex)
    assert (path is not None), "Path cannot be None."
    assert (len(path) > 0), "Path cannot be empty."
    return path
    return [1,2]

def dfs_to_target(objIndex, graph, stack):
    assert(graph is not None), "Graph is None"
    assert(objIndex >= 0 and objIndex < len(graph)), "Target index is not a valid index"
    assert(stack is not None), "Stack cannot be None"
    parent = [-1] * len(graph)
    visited = list()
    objIndexFound = False
    currentIndex = -1
    while(stack and not objIndexFound):
        # (1): Pop Node
        currentIndex = stack.pop()

        # (2): if curr node not in visited, mark it visited
        if(currentIndex not in visited):
            visited.append(currentIndex)
            if(currentIndex == objIndex):
                objIndexFound = True
            else:
                # (3): Update unvisited neighbors
                for neighbor in graph[currentIndex][1]:
                    if(neighbor not in visited):
                        # (4): Push unvisited neighbors to stack
                        stack.append(neighbor)
                        if(parent[neighbor] == -1):
                            parent[neighbor] = currentIndex

    if(objIndexFound):
        path = list()
        while(currentIndex != -1):
            path.append(currentIndex)
            currentIndex = parent[currentIndex]
        path.reverse()
        return path
    
    return None
    

def get_dfs_path():
    #print("\DFS has activated")
    assert (global_game_data.current_graph_index is not None), "Current graph index cannot be None."
    assert (graph_data_file.graph_data is not None), "Graph_data cannot be None."
    graphIndex = global_game_data.current_graph_index
    assert (graph_data_file.graph_data[global_game_data.current_graph_index] is not None), "Graph_data at graph index cannot be None."
    graph = graph_data_file.graph_data[graphIndex]

    #Intializing and declaring objective variables
    targetIndex = global_game_data.target_node[graphIndex]
    endIndex = len(graph) - 1

    #Intializing and declaring variable for Path
    pathStartToEnd = list()

    #Start to Target DFS Path

    #Intializing Stack for Start to Target DFS
    stack = [0]
    pathsToTarget = dfs_to_target(targetIndex, graph, stack)
    
    

    #Transferring path into one path
    assert(pathsToTarget is not None), "Path from start to target is None"
    assert (len(pathsToTarget) > 0), "Path from start to target cannot be empty."
    for x in range(1, len(pathsToTarget)):
        pathStartToEnd.append(pathsToTarget[x])


    #Target To End

    #Intializing Stack for Target to End DFS
    stack.clear
    stack = [targetIndex]

    #Target to End DFS Path
    pathTargetToEnd = dfs_to_target(endIndex, graph, stack)

    #Transferring the pathTargetToEnd to pathStartToEnd
    assert(pathTargetToEnd is not None), "Path from target to end is None"
    assert (len(pathTargetToEnd) > 0), "Path from target to end cannot be empty."
    for x in range(1, len(pathTargetToEnd)):
        pathStartToEnd.append(pathTargetToEnd[x])
 



    assert (pathStartToEnd is not None), "Path cannot be None."
    assert (len(pathStartToEnd) > 0), "Path cannot be empty."
    assert targetIndex in pathStartToEnd
    assert pathStartToEnd[len(pathStartToEnd) - 1] == endIndex
    for i in range(len(pathStartToEnd) - 1):
        assert pathStartToEnd[i + 1] in graph[pathStartToEnd[i]][1]
    
    return pathStartToEnd
    return [1,2]

def bfs_to_target(objIndex, graph, stack):
    assert(graph is not None), "Graph is None"
    assert(objIndex >= 0 and objIndex < len(graph)), "Target index is not a valid index"
    assert(stack is not None), "Stack cannot be None"
    parent = [-1] * len(graph)
    visited = list()
    objIndexFound = False
    currentIndex = -1
    while(stack and not objIndexFound):
        # (1): Pop Node
        currentIndex = stack.pop()

        # (2): if curr node not in visited, mark it visited
        if(currentIndex not in visited):
            visited.append(currentIndex)
            if(currentIndex == objIndex):
                objIndexFound = True
            else:
                # (3): Update unvisited neighbors
                for neighbor in graph[currentIndex][1]:
                    if(neighbor not in visited):
                        # (4): Push unvisited neighbors to stack
                        stack.insert(0, neighbor)
                        if(parent[neighbor] == -1):
                            parent[neighbor] = currentIndex

    if(objIndexFound):
        path = list()
        while(currentIndex != -1):
            path.append(currentIndex)
            currentIndex = parent[currentIndex]
        path.reverse()
        return path
    
    return None

def get_bfs_path():
    #print("\BFS has activated")
    assert (global_game_data.current_graph_index is not None), "Current graph index cannot be None."
    assert (graph_data_file.graph_data is not None), "Graph_data cannot be None."
    graphIndex = global_game_data.current_graph_index
    assert (graph_data_file.graph_data[global_game_data.current_graph_index] is not None), "Graph_data at graph index cannot be None."
    graph = graph_data_file.graph_data[graphIndex]

    #Intializing and declaring objective variables
    targetIndex = global_game_data.target_node[graphIndex]
    endIndex = len(graph) - 1

    #Intializing and declaring variable for Path
    pathStartToEnd = list()

    #Start to Target DFS Path

    #Intializing Stack for Start to Target BFS
    stack = [0]
    pathsToTarget = bfs_to_target(targetIndex, graph, stack)
    
    

    #Transferring path into one path
    assert(pathsToTarget is not None), "Path from start to target is None"
    assert (len(pathsToTarget) > 0), "Path from start to target cannot be empty."
    for x in range(1, len(pathsToTarget)):
        pathStartToEnd.append(pathsToTarget[x])


    #Target To End

    #Intializing Stack for Target to End BFS
    stack.clear
    stack = [targetIndex]

    #Target to End BFS Path
    pathTargetToEnd = bfs_to_target(endIndex, graph, stack)

    #Transferring the pathTargetToEnd to pathStartToEnd
    assert(pathTargetToEnd is not None), "Path from target to end is None"
    assert (len(pathTargetToEnd) > 0), "Path from target to end cannot be empty."
    for x in range(1, len(pathTargetToEnd)):
        pathStartToEnd.append(pathTargetToEnd[x])
 



    assert (pathStartToEnd is not None), "Path cannot be None."
    assert (len(pathStartToEnd) > 0), "Path cannot be empty."
    assert targetIndex in pathStartToEnd
    assert pathStartToEnd[len(pathStartToEnd) - 1] == endIndex
    for i in range(len(pathStartToEnd) - 1):
        assert pathStartToEnd[i + 1] in graph[pathStartToEnd[i]][1]

    return pathStartToEnd
    return [1,2]

class Node:

    def __init__(self, nodeIndex, nodeCoords, adjacent):
        self.nodeIndex = nodeIndex
        self.coords = nodeCoords
        self.adjacent = adjacent
        self.cost = sys.maxsize
    
    
    def getAdjacent(self):
        return self.adjacent
    
    def getCoords(self):
        return self.coords
    
    def getCost(self):
        return self.cost
    
    def getNode(self):
        return self
    
    def getNodeIndex(self):
        return self.nodeIndex
    
    def setCost(self, newCost):
        if self.cost > newCost:
            self.cost = newCost
            return True
        return False


    

def get_cost(currentNode, neighborNode):
    neighborX, neighborY = neighborNode.getCoords()
    currentX, currentY = currentNode.getCoords()
    return math.sqrt((neighborX - currentX) ** 2 + (neighborY - currentY) ** 2) + currentNode.getCost()


def update_priority(heapToAlter, old_priority, new_priority, item):
    for i in range(len(heapToAlter)):
        if heapToAlter[i][1] == item and heapToAlter[i][0] == old_priority:
            heapToAlter[i] = (new_priority, item)
            heap.heapify(heapToAlter)  # Reorder the heap after updating
            break

def dijkstra_to_target(objIndex, graph, nodes, dijkstraHeap):
    assert(graph is not None), "Graph is None"
    assert(objIndex >= 0 and objIndex < len(graph)), "Target index is not a valid index"
    assert(dijkstraHeap is not None), "Stack cannot be None"

    parent = [-1] * len(graph)
    solved = list()
    seenNotSolved = list()
    seenNotSolved.append(dijkstraHeap[0][1])
    objIndexFound = False
    currentIndex = -1
    while(dijkstraHeap and not objIndexFound):
        # (1): Pop Node
        currentIndex = heap.heappop(dijkstraHeap)[1]
        currentNode = nodes[currentIndex]
        
        

        # (2): if curr node not in visited, mark it visited
        if(currentIndex not in solved):
            solved.append(currentIndex)
            seenNotSolved.remove(currentIndex)
            if(currentIndex == objIndex):
                objIndexFound = True
            # (3): Update unvisited neighbors
            for neighbor in currentNode.getAdjacent():
                if(neighbor not in solved):
                    cost = get_cost(currentNode, nodes[neighbor])
                    if(neighbor not in seenNotSolved):
                        seenNotSolved.append(neighbor)
                        parent[neighbor] = currentIndex
                        heap.heappush(dijkstraHeap, (cost, neighbor))
                    else:
                        oldCost = nodes[neighbor].getCost()
                        if(nodes[neighbor].setCost(cost)):
                            parent[neighbor] = currentIndex
                            update_priority(dijkstraHeap, oldCost, cost, neighbor)
                    



    if(objIndexFound):
        path = list()
        while(currentIndex != -1):
            path.append(currentIndex)
            currentIndex = parent[currentIndex]
        path.reverse()
        return path
    
    return None


def get_dijkstra_path():
    assert (global_game_data.current_graph_index is not None), "Current graph index cannot be None."
    assert (graph_data_file.graph_data is not None), "Graph_data cannot be None."
    graphIndex = global_game_data.current_graph_index
    assert (graph_data_file.graph_data[global_game_data.current_graph_index] is not None), "Graph_data at graph index cannot be None."
    graph = graph_data_file.graph_data[graphIndex]

    #Intializing and declaring objective variables
    targetIndex = global_game_data.target_node[graphIndex]
    endIndex = len(graph) - 1

    #Intializing and declaring variable for Path
    pathStartToEnd = list()

    #Start to Target DFS Path

    #Intializing nodes and heapq for Start to Target Dijkstra

    # Give all nodes cost ∞ and mark them “unseen”
    nodes = list()
    for i in range(len(graph)):
        nodes.append(Node(i, graph[i][0], graph[i][1]))

    heapStartToTarget = []
    heap.heapify(heapStartToTarget)
    nodes[0].setCost(0)
    heap.heappush(heapStartToTarget, (nodes[0].getCost(), 0))
    pathsToTarget = dijkstra_to_target(targetIndex, graph, nodes, heapStartToTarget)
    #print(pathsToTarget)
    
    

    #Transferring path into one path
    assert(pathsToTarget is not None), "Path from start to target is None"
    assert (len(pathsToTarget) > 0), "Path from start to target cannot be empty."
    for x in range(1, len(pathsToTarget)):
        pathStartToEnd.append(pathsToTarget[x])


    #Target To End

    #Intializing nodes and heapq for Target to End Dijkstra
    heapTargetToEnd = []
    heap.heapify(heapTargetToEnd)
    nodes[targetIndex].setCost(0)
    heap.heappush(heapTargetToEnd, (nodes[targetIndex].getCost(), targetIndex))
    #print(heapTargetToEnd)

    #Target to End BFS Path
    pathTargetToEnd = dijkstra_to_target(endIndex, graph, nodes, heapTargetToEnd)

    #Transferring the pathTargetToEnd to pathStartToEnd
    assert(pathTargetToEnd is not None), "Path from target to end is None"
    assert (len(pathTargetToEnd) > 0), "Path from target to end cannot be empty."
    for x in range(1, len(pathTargetToEnd)):
        pathStartToEnd.append(pathTargetToEnd[x])
 

    print(f"Start to end: {pathStartToEnd}")
    assert (pathStartToEnd is not None), "Path cannot be None."
    assert (len(pathStartToEnd) > 0), "Path cannot be empty."
    assert targetIndex in pathStartToEnd
    assert pathStartToEnd[len(pathStartToEnd) - 1] == endIndex
    for i in range(len(pathStartToEnd) - 1):
        assert pathStartToEnd[i + 1] in graph[pathStartToEnd[i]][1]

    return pathStartToEnd
