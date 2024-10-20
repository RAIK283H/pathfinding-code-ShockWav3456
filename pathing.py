import graph_data as graph_data_file
import global_game_data
from numpy import random


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

#DFS(u)
    #for each neighbor v of u
    #   if v is unvisited, tree edge, DFS(v)
    #   else if v is explored, bidirectional/back edge
    #   else if v is visited, forward/cross edge

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
    return pathStartToEnd
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
