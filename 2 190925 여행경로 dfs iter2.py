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
    stack = [(i, visited)]
    while stack:
        i, visited = stack.pop()
        visited[i] = max(visited) + 1
        if -1 not in visited:
            answers.append(visited)
            continue
        adjacents = [j for j in range(len(tickets)) if tickets[j][0] == tickets[i][1]]
        for j in adjacents:
            if visited[j] == -1:
                stack.append((j, deepcopy(visited)))

def solution(tickets):
    answers = []
    visited = [-1 for ticket in tickets]
    for i in range(len(tickets)):
        if visited[i] == -1 and tickets[i][0] == "ICN":
            dfs(i, deepcopy(visited), tickets, answers)
    return selectPath(answers, tickets)

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution(tickets))
