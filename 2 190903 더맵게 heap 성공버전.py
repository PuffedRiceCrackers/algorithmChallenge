from heapq import heapify, heappop, heappush
def solution(scoville, K):
    heapify(scoville)
    count = 0
    while True:
        min1 = heappop(scoville)
        if min1 >= K:
            return count
        elif len(scoville) == 0:
            return - 1
        min2 = heappop(scoville)
        count += 1
        heappush(scoville, min1 + min2 * 2)
        
scoville = [1, 2, 3, 9, 10, 12]
scoville = [7]
K = 7

print(solution(scoville, K))