def solution(brown, red):
    rHeight = [i for i in range(1, red + 1) if red % i == 0 and i <= red / i]
    answer = [[(red / rH) + 2, rH + 2] for rH in rHeight if ((red / rH) + 2) * 2 + rH * 2 == brown]
    return answer[0]

print(solution(10, 2))