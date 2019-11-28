from collections import deque
from copy import deepcopy

def selectPath(paths, tickets):
    answers = []
    for path in paths:
        stringPath = ['ICN']
        for order in range(len(tickets)):
            stringPath.append(tickets[path.index(order)][1])
        answers.append(stringPath)
    answers.sort()
    return answers[0]

def bfs(i, visited, tickets, answers):
    queue = deque([(i, visited)])
    while queue:
        i, visited = queue.popleft()
        visited[i] = max(visited) + 1
        if -1 not in visited:
            answers.append(visited)
            continue
        for j in range(len(tickets)):
            if (visited[j] == -1) and (j in [j for j in range(len(tickets)) if tickets[j][0] == tickets[i][1]]):
                queue.append((j, deepcopy(visited)))
    
def solution(tickets):
    answers = []    
    visited = [-1 for ticket in tickets]
    for i in range(len(tickets)):
        if visited[i] == -1 and (i in [i for i in range(len(tickets)) if tickets[i][0] == "ICN"]):
            bfs(i, deepcopy(visited), tickets, answers)
    return selectPath(answers, tickets)

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution(tickets))