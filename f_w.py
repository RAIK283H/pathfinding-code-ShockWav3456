import global_game_data
from graph_data import graph_data
from scoreboard import Scoreboard
from graph import Graph
from player_object import Player
import random
import graph_data as graph_data_file
import global_game_data
from numpy import random
import sys
import math
import pathing

class F_W:

    def get_distance(currentNode, neighborNode):
        neighborX, neighborY = neighborNode[0]
        currentX, currentY = currentNode[0]
        return math.sqrt((neighborX - currentX) ** 2 + (neighborY - currentY) ** 2)

    # update rule: dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    #
    def graphToMatrix(graph):
        assert(graph is not None), "Graph is None"
        numNodes = len(graph)

        #Nodes aren't adjacent
        notAdjacent = sys.maxsize

        #Distance matrix
        dist = [[notAdjacent] * numNodes for num in range(numNodes)]

        for i in range(numNodes):
            dist[i][i] = 0

        #Establishing dist for adjacent nodes
        for x in range(numNodes):
            for y in range(numNodes):
                if (x != y and y in graph[x][1]):
                    dist[x][y] = F_W.get_distance(graph[x], graph[y])


        return dist
    
    def floyd_WarshallAlgorithm(distMatrix):
        parnMatrix = [[None] * len(distMatrix) for _ in range(len(distMatrix))]
        numNodes = len(distMatrix)

        for i in range(numNodes):
            for j in range(numNodes):
                if distMatrix[i][j] != sys.maxsize:
                    parnMatrix[i][j] = i if i != j else None

        for node in range(numNodes):
            for x in range(numNodes):
                for y in range(numNodes):
                    #I'm spining right round
                    dist = distMatrix[x][node] + distMatrix[node][y]
                    if distMatrix[x][y] > dist:
                        distMatrix[x][y] = dist
                        parnMatrix[x][y] = node
        return parnMatrix

    def getPath(parnMatrix, start, target):
        assert(start in range(len(parnMatrix))), "Start is not in range"
        assert(target >= 0 and target < len(parnMatrix)), "Target index is not a valid index"
        assert(parnMatrix[start][target] is not None), "Path to target is unreachable"
        assert(target)
        #Path
        path = []

        current = target
        while current != start:
            #Add the path in
            path.insert(0, current)
            current = parnMatrix[start][current]

        return path
    
    def floyd_Warshall(targetIndex):
        #Setup testing
        assert (global_game_data.current_graph_index is not None), "Current graph index cannot be None."
        assert (graph_data_file.graph_data is not None), "Graph_data cannot be None."
        graphIndex = global_game_data.current_graph_index
        assert (graph_data_file.graph_data[global_game_data.current_graph_index] is not None), "Graph_data at graph index cannot be None."
        graph = graph_data_file.graph_data[graphIndex]

        #Targets
        endTarget = len(graph) - 1

        #Dist
        distMatrix = F_W.graphToMatrix(graph)

        #Parent
        


        #Applying the floyd
        parnMatrix = F_W.floyd_WarshallAlgorithm(distMatrix)

        pathOriginToTarget = F_W.getPath(parnMatrix, 0, targetIndex)
        pathTargetToEnd = F_W.getPath(parnMatrix, targetIndex, endTarget)


        pathStartToEnd = list()
        #Transferring path into one path
        assert(pathOriginToTarget is not None), "Path from start to target is None"
        assert (len(pathOriginToTarget) > 0), "Path from start to target cannot be empty."
        for x in range(len(pathOriginToTarget)):
            pathStartToEnd.append(pathOriginToTarget[x])

        #Transferring the pathTargetToEnd to pathStartToEnd
        assert(pathTargetToEnd is not None), "Path from target to end is None"
        assert (len(pathTargetToEnd) > 0), "Path from target to end cannot be empty."
        for x in range(len(pathTargetToEnd)):
            pathStartToEnd.append(pathTargetToEnd[x])

        return pathStartToEnd