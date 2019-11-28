def dfs(i, visited, computers):
    visited[i] = True
    for j in range(len(computers[i])):
        if computers[i][j] == 1 and visited[j] == False:
            dfs(j, visited, computers)

def solution(n, computers):
    visited = [False for i in range(n)]
    numConn = 0
    for i in range(len(computers)):
        if visited[i] == False:
            numConn += 1
            dfs(i, visited, computers)
    return numConn

numComputers = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(numComputers, computers))