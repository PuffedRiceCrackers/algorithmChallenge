def solution(n, m, s1, s2, cache):
    #base case
    if n == len(s1) - 1:
        return 1 if s1[n] in s2[m:] else 0
    if m == len(s2) - 1:
        return 1 if s2[m] in s1[n:] else 0
    answer = cache[n][m]
    if answer == -1:
        if s1[n] == s2[m]:
            answer = 1 + solution(n+1, m+1, s1, s2, cache)
        else:
            answer = max(solution(n+1, m, s1, s2, cache), solution(n, m+1, s1, s2, cache))
        cache[n][m] = answer
    return answer

def longestCommonSubsequence(s1, s2):
    if s1 == "" or s2 == "":
        return 0
    cache = [[-1 for j in range(len(s2))] for i in range(len(s1))]
    return solution(0, 0, s1, s2, cache)

print(longestCommonSubsequence("bsb", "bkj"))