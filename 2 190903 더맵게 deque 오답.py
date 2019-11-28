from collections import deque

def solution(scoville, K):
    scoville = deque(scoville)
    if min(scoville) < K:
        if len(scoville) == 1:
            return - 1
        else:
            min1 = scoville.popleft
            min2 = scoville.popleft
            scoville.appendleft(min1 + (min2 * 2))
            count += 1
            scoville.sort()
    count = 0
    return count