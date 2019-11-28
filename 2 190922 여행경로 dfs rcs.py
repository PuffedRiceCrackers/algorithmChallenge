from collections import deque
from copy import deepcopy

def dfs(tickets, start, visited, sol):
    if visited == None:
        visited = set()
    visited.add(start)
    for nextVertex in set(i for i in range(len(tickets)) if tickets[i][0] == tickets[start][1]) - visited:
        path = dfs(tickets, nextVertex, deepcopy(visited), sol)
        if len(path) == len(tickets):
            sol.append(path)
    return visited
    
def solution(tickets):
    startTickets = [i for i in range(len(tickets)) if tickets[i][0] == "ICN"]
    sol = []
    for start in startTickets:
        dfs(tickets, start, None, sol)
    return sol

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))