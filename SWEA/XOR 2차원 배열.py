N, M = map(int, input().split())

grid = []

for i in range(N):
    grid.append([])
    tmp = input()
    for s in tmp:
        grid[i].append(s)
        
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[False for _ in range(M)] for _ in range(N)]

flag = False


def dfs(c_x, c_y, flag):
    
    for i in range(4):
        
        n_x = c_x + dx[i]
        n_y = c_y + dy[i]
        
        if (0 <= n_x < N) and (0 <= n_y < M):
            if not visited[n_x][n_y]:
                if grid[n_x][n_y] == "?":
                    grid[n_x][n_y] = "#" if grid[c_x][c_y] == "." else "."
                    visited[n_x][n_y] = True
                    dfs(n_x, n_y, flag)
                else:
                    if grid[c_x][c_y] == grid[n_x][n_y]:
                        flag = True      
                    visited[n_x][n_y] = True
                    dfs(n_x, n_y, flag)
                    
dfs(0,0,flag)
if flag:
    print(f" impossible")
else:
    print(f"# possible")
                    
               
                    