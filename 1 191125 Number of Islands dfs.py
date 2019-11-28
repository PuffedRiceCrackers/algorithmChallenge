s = """11000
11000
00100
00011
"""

def dfs(row,  col, visited, grid):
    visited[row][col] = True
    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= r < len(grid) and 0 <= c < len(grid[r]):
            if visited[r][c] == False and grid[r][c] == '1':
                dfs(r, c, visited, grid)

def solution(grid):

    # 만약 grid가 string인 경우
    # temp = []
    # for line in gird.splitlines():
    #     temp.append(list(line))
    # grid = temp

    visited = [[False for col in grid[i]] for i in range(len(grid))]
    island = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if visited[row][col] == False and grid[row][col] == '1':
                dfs(row, col, visited, grid)
                island += 1
    return island