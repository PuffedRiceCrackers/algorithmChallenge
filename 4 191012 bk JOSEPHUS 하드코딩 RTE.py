def solution(N, K):
    alive = [i for i in range(N)]
    turn = 0
    while len(alive) != 2:
        del alive[turn]
        turn = (turn + K - 1) % len(alive)
    alive = list(map(lambda x: x + 1, alive))
    print(f"{alive[0]} {alive[1]}")

tests = int(input())
for test in range(tests):
    N, K = map(int, input().split())
    solution(N, K)

