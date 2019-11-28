def solution(A, a, b):
    if b <= a:
        try:
            return A[a]
        except:
            return ''
    else:
        prefix = ''
        for m, n in zip(list(solution(A, a, int((a + b) / 2))), list(solution(A, int((a + b) / 2) + 1, b))):
            if m == n:
                prefix += m
            else:
                break
        return prefix

print(solution(["flower","flow","flooo"], 0, 2))


    
