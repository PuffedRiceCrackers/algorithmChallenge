def solution(n):
    count = 0
    for k in range(1, n + 1):
        x = (1 / 2) * ((n * 2 / k) - k + 1)
        if int(x) == x and x > 0:
            count += 1
    return count

solution(15)