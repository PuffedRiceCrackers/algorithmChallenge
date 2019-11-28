import math

def returnCount(planetPos, start, dest):
    count = 0
    detail = []
    for planet in planetPos:
        radius = planet[2]
        distFromStart = math.sqrt(math.pow(planet[0] - start[0], 2) + math.pow(planet[1] - start[1], 2))
        distFromDest = math.sqrt(math.pow(planet[0] - dest[0], 2) + math.pow(planet[1] - dest[1], 2))
        if ((distFromStart < radius) and (distFromDest > radius)) or ((distFromStart > radius) and (distFromDest < radius)):
            count += 1
    return count

numTestCases = int(input())
resultList = []
for testCase in range(numTestCases):

    # start, dest, planetPos
    startDestSpotList = list(map(int, input().split()))
    start = startDestSpotList[:2] #[1,2]
    dest = startDestSpotList[2:]  #[3,4]
    numPlanets = int(input())
    planetPos = []
    for planet in range(numPlanets):
        planetPos.append(list(map(int, input().split())))

    # min num of planets to pass
    resultList.append(returnCount(planetPos, start, dest))

for result in resultList:
    print(result)


