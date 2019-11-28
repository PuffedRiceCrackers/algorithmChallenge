from collections import deque
from itertools import islice
from copy import deepcopy

def calcFinish(progresses, speeds):
    finished = [ i for i in range(len(progresses))]
    for progress, speed, i in zip(progresses, speeds, finished):
        daysLeft = (100 - progress) / speed
        if daysLeft - int(daysLeft) != 0:
            daysLeft = int(daysLeft) + 1
        finished[i] = [daysLeft, i]
    return deque(finished)

def solution(progresses, speeds):
    schedule = calcFinish(progresses, speeds)
    answer = []
    schedulecopy = deepcopy(schedule)
    while schedule:
        time, nr = schedule.popleft()
        onList = [nr]
        for pair in islice(schedulecopy, nr + 1, len(schedulecopy) + 1):
            if pair[0] <= time and pair[1] - 1 in onList: 
                schedule.popleft()
                onList.append(pair[1])
            else:
                break
        answer.append(len(onList))
    return answer

# progresses = [40, 93, 30, 55, 60, 65]
# speeds = [60, 1, 30, 5 , 10, 7]
# 완료순서 (기능번호) 0→2→4→5→1→3
# return : [1,2,3]

progresses = [93, 30, 55, 60, 40, 65]
speeds = [1, 30, 5, 10, 60, 7]
# 완료순서 (기능번호) : 4→1→3→5→0→2
# return : [2,4]



print(solution(progresses, speeds))