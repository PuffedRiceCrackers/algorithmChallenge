from collections import deque
def solution(n, computers):
    explored = [False for computer in computers]
    network = 0
    for i in range(len(computers)): 
        if explored[i] == False:
            stack = deque([])
            stack.append(i)
            while stack:
                target = stack.pop()
                explored[target] = True
                for j in range(len(computers[target])):
                    if computers[target][j] == 1 and explored[j] == False:
                        stack.append(j)
            network += 1
    return network

#computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	 
#computers = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 1, 1, 0], [0, 0, 1, 0, 1]]
#computers = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
computers = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
n = len(computers)
print(solution(n, computers))

# 밑은 대부분은 맞았지만 두 개 케이스가 틀렸던 버전. 아직도 왜 틀렸는지는 모름. 그러나 intractable하니까 문제
def solution2(n, computers):
    network = [i for i in range(n)]           # 자기자신의 network 번호를 각자 가지고 있음
    for i in range(len(computers)):           # i 컴퓨터의
        for j in range(len(computers[i])):    # j 컴퓨터와의 커넥션
            if computers[i][j] == 1:          # 커넥션이 있다 -> 둘중 작은 네트워크를 선택해서 각자의 네트워크로 하자
                network[i] = min(network[i], network[j])
                network[j] = min(network[i], network[j])
    return len(set(network))
