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
    #print("\nRandom has activated")
    assert (global_game_data.current_graph_index is not None), "Current graph index cannot be None."
    assert (graph_data_file.graph_data is not None), "Graph_data cannot be None."
    graphIndex = global_game_data.current_graph_index
    assert (graph_data_file.graph_data[graphIndex] is not None), "Graph_data at graph index cannot be None."
    
    lastIndex = 0
    currentIndex = 0
    nextIndex = -1

    targetIndex = global_game_data.target_node[graphIndex]
    endIndex = len(graph_data_file.graph_data[graphIndex]) - 1

    reachedTarget = False
    reachedEnd = False

    path = list()
    while(not reachedTarget and not reachedEnd): #):#
        #print("\nTriggered loop main")
        #Run path search
        while(not reachedTarget):
            if(currentIndex == targetIndex):
                reachedTarget = True
                #print("\n Trigger Reached target path")
            else:
                numberOfAdjacentSpaces = len(graph_data_file.graph_data[graphIndex][currentIndex][1])

                nextIndex = graph_data_file.graph_data[graphIndex][currentIndex][1][random.randint(0, numberOfAdjacentSpaces)]

                if(numberOfAdjacentSpaces != 1):
                    #print("\nTarget inner while")
                    while(lastIndex == nextIndex or currentIndex == nextIndex):
                        nextIndex = graph_data_file.graph_data[graphIndex][currentIndex][1][random.randint(0, numberOfAdjacentSpaces)]

                #print(f"\nLast Last Index = {lastlastIndex} | Last Index = {lastIndex} | Current Index = {currentIndex} | Next Index = {nextIndex} | Evaluation of while left = {lastlastIndex == currentIndex} | Evaluation of while right = {lastIndex == currentIndex} |Evaluation of while = {lastlastIndex == currentIndex and lastIndex == currentIndex}  | Number of Adjacent = {numberOfAdjacentSpaces} | Adjacent Space eval = {numberOfAdjacentSpaces != 1}\n")
                lastIndex = currentIndex
                currentIndex = nextIndex
                path.append(currentIndex)
                #print("\nTarget end")
        #print("\n Triggered Reach end loop")
        while(not reachedEnd):
            if(currentIndex == endIndex):
                reachedEnd = True
                #print("\n Trigger Reached end path")
            else:
                numberOfAdjacentSpaces = len(graph_data_file.graph_data[graphIndex][currentIndex][1])

                nextIndex = graph_data_file.graph_data[graphIndex][currentIndex][1][random.randint(0, numberOfAdjacentSpaces)]

                if(numberOfAdjacentSpaces != 1):
                    #print("\nTarget end while")
                    while(lastIndex == nextIndex or currentIndex == nextIndex):
                        nextIndex = graph_data_file.graph_data[graphIndex][currentIndex][1][random.randint(0, numberOfAdjacentSpaces)]

                #print(f"\nLast Last Index = {lastlastIndex} | Last Index = {lastIndex} | Current Index = {currentIndex} | Next Index = {nextIndex} | Evaluation of while left = {lastlastIndex == currentIndex} | Evaluation of while right = {lastIndex == currentIndex} |Evaluation of while = {lastlastIndex == currentIndex and lastIndex == currentIndex}  | Number of Adjacent = {numberOfAdjacentSpaces} | Adjacent Space eval = {numberOfAdjacentSpaces != 1}\n")
                lastIndex = currentIndex
                currentIndex = nextIndex
                path.append(currentIndex)
                #print("\End end")
    assert (path is not None), "Path cannot be None."
    assert (len(path) > 0), "Path cannot be empty."
    return path
    return [1,2]


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
