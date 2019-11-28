# limit 조절하면 정답개수가 달라지는걸 보니 recursion depth 가 너무 커져서 RTE 나는 듯 함

from math import inf
import sys
sys.setrecursionlimit(20000)
N = int(input())
poison = list(map(int, input().split()))
poison.insert(0, 0)
cache = [[-1 for i in range(len(poison))] for j in range(len(poison))]
def solution(start,end):
    global poison
    global cache
    if end - 2 <= start <= end:
        return poison[start]
    elif end < start:
        return inf
    answer = cache[start][end]
    one, two, three = inf, inf, inf
    if answer == -1:
        try:
            one = poison[start] + solution(start + 1, end)
            two = poison[start] + solution(start + 2, end)
            three = poison[start] + solution(start + 3, end)
        except:
            pass
        answer = min(one, two, three)
        cache[start][end] = answer
    return answer
    
"""
3 1 1 7 4 9 3
7 8 9 10 9 8 7 6 5 4
100 100 0 100 0 100 100 0 0 100 100 100
"""

print(solution(0, len(poison) - 1)) 

        






