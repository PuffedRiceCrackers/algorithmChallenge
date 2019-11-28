def binarySearch(uniqueScore, aliceTotal):
    minIdx = 0
    maxIdx = len(uniqueScore) - 1
    while minIdx <= maxIdx:
        currIdx = int((minIdx + maxIdx) / 2)
        minIdx = currIdx + 1 if uniqueScore[currIdx] > aliceTotal else minIdx
        maxIdx = currIdx - 1 if uniqueScore[currIdx] < aliceTotal else maxIdx
        if uniqueScore[currIdx] == aliceTotal:
            return currIdx + 1
    if maxIdx == -1:
        return 1
    else:
        return maxIdx + 2

def climbingLeaderboard(scores, alice):
    uniqueScore = list(set(scores))
    uniqueScore.sort(reverse=True)
    return [binarySearch(uniqueScore, aliceScore) for aliceScore in alice]
    

uniqueScores = 7# int(input())
scores = [100,100,95]#list(map(int, input().split()))
alicePlayed = 4#int(input())
alice = [5, 94, 3]  #list(map(int, input().split()))

scores = list(map(int, ("100 90 90 80 75 60").split()))
alice = list(map(int, ("50 65 77 90 102").split()))

print(climbingLeaderboard(scores, alice))

# def climbingLeaderboard(scores, alice):
#     uniqueScore = list(set(scores))
#     uniqueScore.sort(reverse=True)
#     print(uniqueScore)
#     def binarySearch(uniqueScore, aliceTotal):
#         print('')
#         minIdx = 0
#         maxIdx = len(uniqueScore) - 1
#         while minIdx <= maxIdx:
#             currIdx = int((minIdx + maxIdx) / 2)
#             print(f" 1 : minIdx : {minIdx}, maxIdx : {maxIdx}, alice : {aliceTotal}, currIdx : {currIdx}")
#             minIdx = currIdx + 1 if uniqueScore[currIdx] > aliceTotal else minIdx
#             maxIdx = currIdx - 1 if uniqueScore[currIdx] < aliceTotal else maxIdx
#             if uniqueScore[currIdx] == aliceTotal:
#                 return currIdx + 1
#         print(f" 2 : minIdx : {minIdx}, maxIdx : {maxIdx}, alice : {aliceTotal}, currIdx : {currIdx}")
#         if maxIdx == -1:
#             return 1
#         else:
#             return maxIdx + 2
#     return [binarySearch(uniqueScore, aliceScore) for aliceScore in alice]


    

    

    
    

        

# aliceTotal = 0
# for i in range(len(alice)):
#     aliceTotal += alice[i]

# binarySearch(uniqueScore, aliceTotal)

