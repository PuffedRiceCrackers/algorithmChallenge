
def solution(n):
    target = bin(n).count('1')
    while True:
        n = n + 1
        if bin(n).count('1') == target:
            return n

n = 78
print(solution(n))