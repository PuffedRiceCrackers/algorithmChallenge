def solution(s):
    temp = list(map(int, s.split()))
    return str(min(temp)) + " " + str(max(temp))

s = "-1 -2 -3 -4"
print(solution(s))