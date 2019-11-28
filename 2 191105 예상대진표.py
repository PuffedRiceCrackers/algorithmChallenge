
from math import ceil
def solution(n, a, b):
    count = 0
    while True:
        count += 1
        a = ceil(a / 2)
        b = ceil(b / 2)
        if abs(a - b) < 1:
            break
    return count

N = 8
A = 4
B = 7

print(solution(N,A,B))
