from collections import deque
from copy import deepcopy
def solution(tickets):
    answers = []
    seedTickets = [(tickets[i], i) for i in range(len(tickets)) if tickets[i][0] == "ICN"]  # [([ICN, SFO],0),(ICN, ATL,1)
    for seed in seedTickets: 
        visited = [-1 for ticket in tickets]
        visitOrder = 0
        queue = deque()
        queue.append([seed, deepcopy(visited)])
        while (queue):
            ticket, visited = queue.pop()
            if -1 in visited:
                visitOrder = max(visited) + 1
                visited[ticket[1]] = visitOrder
                destination = ticket[0][1]
                for i in range(len(tickets)):
                    if tickets[i][0] == destination and visited[i] == -1:
                        queue.append([(tickets[i], i), deepcopy(visited)])
            answer = ['ICN']
            if -1 not in visited:
                for i in range(len(tickets)):
                    answer.append(tickets[visited.index(i)][1])
                answers.append(answer)
    answers.sort()
    return answers[0]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))