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

def dfs(i, visited, tickets, answers):
    visited[i] = max(visited) + 1
    dest = tickets[i][1]
    for j in range(len(tickets)):
        if visited[j] == -1 and tickets[j][0] == dest:
            dfs(j, deepcopy(visited), tickets, answers)
    if - 1 not in visited:
        answers.append(visited)

def solution(tickets):
    answers = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            visited = [-1 for ticket in tickets]
            dfs(i, visited, tickets, answers)
    return selectPath(answers, tickets)

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))
