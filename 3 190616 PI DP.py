# RUN TIME ERROR 로 실패함
def calcChunk(numList):  # 3개~5개만 넘겨주었을 때, 최소 level 반납

    lastIdx = len(numList) - 1
    # level 1?
    first = numList[0]
    for idx in range(lastIdx + 1):
        if numList[idx] != first:
            break
        if idx == lastIdx:
            return 1
    
    # level 2?
    plusTemp = numList[0]
    for idx in range(1, lastIdx + 1):
        if numList[idx] != plusTemp + 1:
            break
        else:
            plusTemp = numList[idx]
        if idx == lastIdx:
            return 2
    minusTemp = numList[0]
    for idx in range(1, lastIdx + 1):
        if numList[idx] != minusTemp - 1:
            break
        else:
            minusTemp = numList[idx]
        if idx == lastIdx:
            return 2
    
    # level 4?
    first, second = numList[0], numList[1]
    temp = first
    for idx in range(lastIdx + 1):
        if numList[idx] != temp:
            break
        if idx == lastIdx:
            return 4
        else:
            temp = (temp == first) and second or first
    
    # level 5?
    interval = numList[1] - numList[0]
    previous = numList[0]
    for idx in range(1,lastIdx + 1):
        if numList[idx]-previous != interval:
            break
        if idx == lastIdx:
            return 5
        else:
            previous = numList[idx]
    
    return 10

def minLevelTill(maxIdx):
    global cache
    global sequence

    if maxIdx == 0 or maxIdx == 1:
        return 10
    
    answer = cache[maxIdx]
    
    # if not calculated
    if answer == -1:
        if maxIdx == 2 or maxIdx == 3 or maxIdx == 4:
            answer = calcChunk(sequence[0:maxIdx + 1])
        elif maxIdx == 5:
            answer = minLevelTill(2) + calcChunk(sequence[3:6])
        elif maxIdx == 6:
            answer = min(minLevelTill(2) + calcChunk(sequence[3:7]), minLevelTill(3) + calcChunk(sequence[4:7]))
        else:
            temp = []
            temp.append(minLevelTill(maxIdx - 3) + calcChunk(sequence[maxIdx - 2:maxIdx+1]))
            temp.append(minLevelTill(maxIdx - 4) + calcChunk(sequence[maxIdx - 3:maxIdx+1]))
            temp.append(minLevelTill(maxIdx - 5) + calcChunk(sequence[maxIdx - 4:maxIdx+1]))
            answer = min(temp)
        cache[maxIdx] = answer
    return answer
    
tests = int(input())
answers = []
for test in range(tests):
    sequence = list(map(int,list(input())))
    length = len(sequence)
    cache = [-1 for i in range(length)]
    answers.append(minLevelTill(length - 1))

for answer in answers:
    print(answer)
