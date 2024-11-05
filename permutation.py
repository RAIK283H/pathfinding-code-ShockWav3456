import copy
import math

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def getLargestMobileInt(nodeArray, movementArray):
    print(nodeArray)
    print(movementArray)
    #Int to track the largest mobile int index
    largestMobileIntIndex = -1
    largestMobileInt = -1

    #Search for largest mobile int
    for i in range(len(nodeArray)):
        print(f"\n\nLoop index = {i}")
        #Gets the index of the value you need to compare
        #   if movementArray[i] is true, you need to check the value to the left (i=1)
        #   else you need to check the value to the right (i+1)

        compareIndex = (i - 1) if movementArray[i] else (i + 1)
        print(f"\tIs compare index correct: {(compareIndex == (i -1 if movementArray[i] else i + 1))} | movementArray[i] = {movementArray[i]} | compareIndex = {compareIndex} | current index = {i}")
        print(f"\tIs compare index valid: {0 <= compareIndex < len(nodeArray)}")
        #Checking if compare index is a valid index
        if(0 <= compareIndex < len(nodeArray)):
            print(f"\tIs nodeArray[i] greater than nodeArray[compareIndex]: {nodeArray[i] > nodeArray[compareIndex]} | nodeArray[i] = {nodeArray[i]} | nodeArray[compareIndex] = {nodeArray[compareIndex]}")
            #is nodeArray[i] greater than the value it points at
            if(nodeArray[i] > nodeArray[compareIndex]):
                #Is nodeArray[i] greater than the value of the current Mobile Index?
                print(f"\tIs nodeArray[i] greater than mobile Int: {nodeArray[i] > largestMobileInt} | nodeArray[i] = {nodeArray[i]} | largestMobileInt = {largestMobileInt}")
                if(nodeArray[i] > largestMobileInt):
                    #Since nodeArray[i] is a mobile int and larger than the current one,
                    # change the index to i
                    largestMobileIntIndex = i
                    largestMobileInt = nodeArray[i]

    #If the largest mobile Int index is -1, it means value wasn't found
    if(largestMobileIntIndex == -1):        
        return None
    
    #The largest mobile index was found
    else:
        return largestMobileIntIndex



def permutationGenerator(lengthOfArray):
    # The list that will hold all the permutations
    permutations = []
    
    #The array that shows the direction of that the same index in nodeArray is pointing
    #True means that the index is moving to the left
    movementArray = [True] * lengthOfArray

    #Array of the nodes, in order of least to greatest
    nodeArray = [None] * lengthOfArray

    #filling the nodeArray with the correct values
    for i in range(lengthOfArray):
        nodeArray[i] = i
    
    #Puts the intial state of nodeArray into the permutations list
    permutations.append(nodeArray.copy())


    #######################
    ## Starting the SJT  ##
    #######################
    

    #SJT will start with a mobile integer
    mobileIntPresent = True
    x = 1
    #Loop through list to generate permutations
    while(mobileIntPresent):

        #Get the index of the mobile integer
        mobileIntIndex = getLargestMobileInt(nodeArray, movementArray)

        #Ensure that a mobile int was actually found
        if(mobileIntIndex is not None):
            #Don't need to check if the index for indexToSwapWith is valid, beacuse it is handled within the getlargestMobileInt method
            indexToSwapWith = mobileIntIndex - 1 if movementArray[mobileIntIndex] else mobileIntIndex + 1
            
            #Swapping the indexs at mobileIntIndex and indexToSwapWith in nodeArray
            swap(nodeArray, mobileIntIndex, indexToSwapWith)
            #Swapping the indexes at mobileIntIndex and indexToSwapWith in movementArray
            swap(movementArray, mobileIntIndex, indexToSwapWith)

            #Switching the direction of all integers with values greater than mobile integer
            
            for i in range(lengthOfArray):
                if(nodeArray[i] > nodeArray[indexToSwapWith]):
                    movementArray[i] = not movementArray[i]

            #Adds this version of nodeArray into permutations
            permutations.append(nodeArray.copy())
        else:
            mobileIntPresent = False
    
    return permutations

def isThereAHamiltonianCycle(graph):
    #generate the permutations
    permutations = permutationGenerator(len(graph))
    #goes through permutations generated
    for permutationIndex in range(len(permutations)):
        #Create shortened variable name for the current permutation
        permutation = permutations[permutationIndex]

        #Goes through current permutation
        for indexOfpermutation in range(len(permutation) - 1):
            #Checks if current node is not in the adjacency list of the next node
            if graph[permutation[indexOfpermutation]] not in graph[permutation[indexOfpermutation + 1]][1]:
                #if current node is not in adjacency list of the next node, not a valid permutation
                del permutations[permutationIndex]
    if(len(permutations) != 0):
        leastDistanceTravled = 10 ** 100
        leastDistanceTravledIndex = -1
        
        for permutationIndex in range(len(permutations)):
            distanceTraveled = 0
            #Create shortened variable name for the current permutation
            permutation = permutations[permutationIndex]
            #Goes through current permutation
            for indexOfpermutation in range(len(permutation) - 1):
                currentNode = graph[permutation[indexOfpermutation]]
                nextNode = graph[permutation[indexOfpermutation + 1]]
                distanceTraveled = math.sqrt(pow(currentNode[0][0] - nextNode[0][0], 2) + pow(currentNode[0][1] - nextNode[0][1], 2))
                if(distanceTraveled < leastDistanceTravled):
                    leastDistanceTravled = distanceTraveled
                    leastDistanceTravledIndex = permutationIndex
        print(f"Optimal distance traveled by a cycle:\033[1m {leastDistanceTravled}\033[0m")
        print(f"Optimal Cycle: {permutations[leastDistanceTravledIndex]}")
        return True
    return None