# Run time error 

import sys
sys.setrecursionlimit(10000)
import math
from itertools import combinations

def powOfAvgError(start, end):
    global cache
    global rawData

    # edge
    if start == end - 1:
        return 0
    if start == end:
        return 0

    # answer
    answer = cache[start][end]

    if answer == -1:
        avg = round(sum(rawData[start:end]) / (end - start))
        answer = 0
        for data in rawData[start:end]:
            answer += math.pow((data - avg), 2)
        cache[start][end] = answer
    return answer

def minOfTotalError():
    global numOfData
    global numberOfEndResult

    minAnswer = 9876543210

    # no lumping is needed
    if numberOfEndResult == 1:
        minAnswer = powOfAvgError(0, numOfData - 1)
    else:
        # Combinaion of lumping numbers
        for combination in list(combinations(list(range(numOfData+1)), numberOfEndResult-1)):
            tempAnswer = 0

            # For each lump, calculate the pow of average error
            for idx in range(len(combination) - 1):
                tempAnswer += powOfAvgError(combination[idx], combination[idx+1])
            tempAnswer += powOfAvgError(0, combination[0])
            tempAnswer += powOfAvgError(combination[-1], numOfData)

            # If the pow of average error of current combination is smaller, replace the old one.
            minAnswer = min(tempAnswer, minAnswer)

    return int(minAnswer)

tests = int(input())
for test in range(tests):
    numOfData, numberOfEndResult = map(int, input().split())
    rawData = list(map(int, input().split()))
    rawData.sort()
    cache = [[-1 for j in range(numOfData + 1)] for i in range(numOfData + 1)]
    print(minOfTotalError())


