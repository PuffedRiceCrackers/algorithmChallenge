







def rcs(n, cache):
    if n == 0 or n==1:
        return 1
    if n == 2:
        return n
    answer = cache[n]
    if answer == -1:
        answer = sum([rcs(i, cache) * rcs(n - i - 1, cache) for i in range(n)])
        cache[n] = answer
    return answer

def solution(n):
    cache = [-1 for i in range(n + 1)]
    return rcs(n, cache)

print(solution(4))