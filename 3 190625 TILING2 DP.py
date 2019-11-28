def count(n):
    
    if n == 0 or n == 1 or n == 2:
        return n
    answer = cache[n]
    if answer == -1:
        answer = count(n-1) + count(n-2)
        cache[n] = answer

    return  answer%1000000007

tests = int(input())
for test in range(tests):
    n = int(input())
    #cache = [[-1 for j in range(n + 2)] for i in range(n + 1)]
    cache = [-1 for i in range(n + 1)]
    
    print(count(n))

# 요건 조합으로 그냥 계산하는건데 너무 계산량이 많아서 돌아가지도 않음
# from itertools import combinations

# def repeatedCombination(a, b):
#     answer = cache[a][b]
#     if answer == -1:
#         x = max(a, b)
#         y = min(a, b)
#         answer = len(list(combinations(range(x + 1), y)))
#         cache[a][b] = answer
#     return answer

# def countCases(n):
#     count = 0
#     for numberOfTwo in range(int(n / 2) + 1):
#         numberOfOne = n - numberOfTwo * 2
#         count += repeatedCombination(numberOfTwo, numberOfOne)
#         print(f"repeatedCombination({numberOfTwo}, {numberOfOne})")
#     return count%1000000007

# tests = int(input())
# for test in range(tests):
#     n = int(input())
#     cache = [[-1 for j in range(n + 2)] for i in range(n + 1)]
#     print(countCases(n))
