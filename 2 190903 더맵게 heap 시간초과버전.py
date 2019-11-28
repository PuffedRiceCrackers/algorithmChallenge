import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while min(scoville) < K:
        if len(scoville) == 1:
            return - 1
        else:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + (min2 * 2))
            count += 1
    return count 

scoville = [5]
K = 7

print(solution(scoville, K))