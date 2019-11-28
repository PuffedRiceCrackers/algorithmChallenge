import sys
sys.setrecursionlimit(1000000)

# Probability of success that snails can climb 'targetHeight' within 'days'
def successRate(days, targetHeight):
    global cache

    if targetHeight <= 1:
        return 1
    if days == 1:
        if targetHeight > 2:
            return 0
        elif targetHeight == 2:
            return 0.75
        elif targetHeight == 1:
            return 0.25
    
    answer = cache[days][targetHeight]

    if answer == -1:
        answer = 0.75 * (successRate(days - 1, targetHeight - 2)) + 0.25 * (successRate(days - 1, targetHeight - 1))
        cache[days][targetHeight] = answer

    return answer
 
tests = int(input())
for test in range(tests):
    height, duration = map(int, input().split())
    cache = [[-1 for j in range(height + 1)] for i in range(duration + 1)] # cache initialized as -1
    print(round(successRate(duration, height),7))


