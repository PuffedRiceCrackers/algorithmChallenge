def solution(s):

    # hol
    hol = []
    for i in range(len(s)):
        j = 0
        while i - j - 1 >= 0 and i + j + 1 <= len(s) - 1:
            if s[i - j - 1] != s[i + j + 1]:
                break
            j += 1
        hol.append(2 * j + 1)

    # jjak
    jjak = []
    for i in range(len(s)):
        j = 0
        while i >= 0 and i + 2 * j + 1 <= len(s) - 1:
            if s[i] != s[i + 2 * j + 1]:
                break
            i -= 1
            j += 1
        jjak.append(2 * j)
        
    return max(max(hol), max(jjak))

print(solution("cbbc"))
