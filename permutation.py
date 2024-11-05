import copy
import math

def swap(array, i, j):
    assert(array is not None), "swap failed: array was None"
    assert(i is not None), "swap failed: i was None"
    assert(j is not None), "swap failed: j was None"
    assert(0 <= i < len(array)), "swap failed: i was not valid index"
    assert(0 <= j < len(array)), "swap failed: j was not valid index"
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def getLargestMobileInt(nodeArray, movementArray):
    assert(nodeArray is not None), "getLargestMobileInt failed: nodeArray was None"
    assert(movementArray is not None), "getLargestMobileInt failed: movementArray was None"
    #Int to track the largest mobile int index
    largestMobileIntIndex = -1
    largestMobileInt = -1

    #Search for largest mobile int
    for i in range(len(nodeArray)):

        #print(f"\n\nLoop index = {i}")

        #Gets the index of the value you need to compare
        #   if movementArray[i] is true, you need to check the value to the left (i=1)
        #   else you need to check the value to the right (i+1)

        compareIndex = (i - 1) if movementArray[i] else (i + 1)

        #print(f"\tIs compare index correct: {(compareIndex == (i -1 if movementArray[i] else i + 1))} | movementArray[i] = {movementArray[i]} | compareIndex = {compareIndex} | current index = {i}")
        #print(f"\tIs compare index valid: {0 <= compareIndex < len(nodeArray)}")

        #Checking if compare index is a valid index
        if(0 <= compareIndex < len(nodeArray)):

            #print(f"\tIs nodeArray[i] greater than nodeArray[compareIndex]: {nodeArray[i] > nodeArray[compareIndex]} | nodeArray[i] = {nodeArray[i]} | nodeArray[compareIndex] = {nodeArray[compareIndex]}")
            
            #is nodeArray[i] greater than the value it points at
            if(nodeArray[i] > nodeArray[compareIndex]):
                #Is nodeArray[i] greater than the value of the current Mobile Index?

                #print(f"\tIs nodeArray[i] greater than mobile Int: {nodeArray[i] > largestMobileInt} | nodeArray[i] = {nodeArray[i]} | largestMobileInt = {largestMobileInt}")

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
    assert(lengthOfArray is not None), "Permutation Generator failed: lengthOfArray was None"
    assert(lengthOfArray > 0), "Permutation Generator failed: lengthOfArray was less than 1"
    lengthOfArray -= 2

    # The list that will hold all the permutations
    permutations = []
    
    #The array that shows the direction of that the same index in nodeArray is pointing
    #True means that the index is moving to the left
    movementArray = [True] * (lengthOfArray)

    #Array of the nodes, in order of least to greatest
    nodeArray = [None] * (lengthOfArray)

    #filling the nodeArray with the correct values
    for i in range(lengthOfArray):
        nodeArray[i] = i + 1
    
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
            #print(f"mobileIntIndex: {mobileIntIndex} indexToSwapWith: {indexToSwapWith}")
            
            #Swapping the indexs at mobileIntIndex and indexToSwapWith in nodeArray
            swap(nodeArray, mobileIntIndex, indexToSwapWith)
            #Swapping the indexes at mobileIntIndex and indexToSwapWith in movementArray
            swap(movementArray, mobileIntIndex, indexToSwapWith)

            #Switching the direction of all integers with values greater than mobile integer
            
            for i in range(lengthOfArray):
                #print(f"i: {i}, indexToSwapWith: {indexToSwapWith}")
                #print(nodeArray)
                if(nodeArray[i] > nodeArray[indexToSwapWith]):
                    movementArray[i] = not movementArray[i]

            #Adds this version of nodeArray into permutations
            permutations.append(nodeArray.copy())
        else:
            mobileIntPresent = False
    
    return permutations

def isThereAHamiltonianCycle(graph):
    assert(graph is not None), "isThereAHamiltonianCycle failed: graph was None"

    permutations = permutationGenerator(len(graph))
    valid_permutations = []

    for permutationIndex in range(len(permutations)):
        permutation = permutations[permutationIndex]
        
        if graph[permutation[len(permutation) - 1]] in graph[permutation[0]][1]:

            is_valid = True

            for indexOfpermutation in range(len(permutation) - 1):
                if graph[permutation[indexOfpermutation]] not in graph[permutation[indexOfpermutation + 1]][1]:
                    is_valid = False
                    break
            
            if is_valid:
                valid_permutations.append(permutation)
        
    if(len(permutations) != 0):
        leastDistanceTraveled = 10 ** 100
        leastDistanceTraveledIndex = -1

    for permutationIndex in range(len(permutations)):
        totalDistanceTraveled = 0
        permutation = permutations[permutationIndex]
        
        for indexOfPermutation in range(len(permutation) - 1):
            currentNode = graph[permutation[indexOfPermutation]]
            nextNode = graph[permutation[indexOfPermutation + 1]]

            distance = math.sqrt(
                (currentNode[0][0] - nextNode[0][0]) ** 2 + 
                (currentNode[0][1] - nextNode[0][1]) ** 2
            )
            totalDistanceTraveled += distance

        if totalDistanceTraveled < leastDistanceTraveled:
            leastDistanceTraveled = totalDistanceTraveled
            leastDistanceTraveledIndex = permutationIndex

        for x in permutations:
            print(x)
        print(f"Optimal distance traveled by a cycle:\033[1m {leastDistanceTraveled}\033[0m")
        print(f"Optimal Cycle: {permutations[leastDistanceTraveledIndex]}")
        return True
    else:
        return False