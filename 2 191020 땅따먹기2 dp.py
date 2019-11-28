# 같은 논리인데 recursion 이라 그런지 시간은 통과 못함

import sys
sys.setrecursionlimit(10000) 

def solution(land):
    cache = [[-1 for j in range(4)] for i in range(len(land))]

    def func(a, b):
        nonlocal cache

        if a == len(land) - 1:
            return land[a][b]

        answer = cache[a][b]

        if answer == -1:
            answer = max([func(a + 1, j) for j in range(4) if j != b]) + land[a][b]
            cache[a][b] = answer
               
        return answer

    return max([func(0, i) for i in range(4)])
    
land = [[1, 2, 300, 5], [5, 6, 7, 100], [4, 3, 2, 100]]
#land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

print(solution(land))         


#land = [[randint(1, 5) for i in range(4)] for i in range(5)]
