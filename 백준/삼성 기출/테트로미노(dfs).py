N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
    
    

visited = [[0 for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
max_v = 0

def dfs(cur, k, sum):
   
    if k == 4:
        global max_v
        max_v = max(max_v, sum)
        return
    
    for x, y in cur:
        for i in range(4):
            
            n_x = x + dx[i]
            n_y = y + dy[i]
            
            if (0 <= n_x < N) and (0 <= n_y < M):
                if visited[n_x][n_y] == 0:
                    visited[n_x][n_y] = 1
                    dfs(cur + [(n_x, n_y)], k+1, sum+grid[n_x][n_y])
                    visited[n_x][n_y] = 0
        
for x in range(N):
    for y in range(M):
        
        visited[x][y] = 1
        dfs([(x,y)], 1, grid[x][y])
        visited[x][y] = 0
        
print(max_v)
