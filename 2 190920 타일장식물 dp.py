
def fib(cache, N):
    if N == 1 or N == 2:
        return 1
    else:
        answer = cache[N]
        if answer != -1:
            return answer
        else:
            cache[N] = fib(cache, N - 1) + fib(cache, N - 2)
            return cache[N]

def solution(N):
    if N == 1:
        return 4
    cache = [-1 for i in range(N + 1)]
    return 2 * (2 * fib(cache, N) + fib(cache, N - 1))
    
print(solution(2))