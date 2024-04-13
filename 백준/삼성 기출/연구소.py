import copy

N, M = map(int, input().split())

grid = []
for i in range(N):
    tmp = list(map(int, input().split()))
    grid.append(tmp)
  
zero_xy = []  
zombie_xy = []
for i in range(N):
    for j in range(M):
        
        if grid[i][j] == 0:
            zero_xy.append((i,j))
        elif grid[i][j] == 2:
            zombie_xy.append((i,j))
        
        
zero_3 = []  

def combination(curr, start):
    
    if len(curr) == 3:
        zero_3.append(curr[:])
        return
    
    for i in range(start, len(zero_xy)):
        curr.append(zero_xy[i])
        combination(curr, i+1)
        curr.pop()

combination([], 0)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def infect(c_grid, x, y):
    
    for i in range(4):
        
        n_x = x + dx[i]
        n_y = y + dy[i]
        
        if (0 <= n_x < N and 0 <= n_y < M):
            if c_grid[n_x][n_y] == 0:
                c_grid[n_x][n_y] = 2
                infect(c_grid, n_x, n_y)
    
max_value = 0

for i in range(len(zero_3)):
    
    c_grid = copy.deepcopy(grid)
    a, b, c = zero_3[i]
    
    #벽세우기
    c_grid[a[0]][a[1]] = 1
    c_grid[b[0]][b[1]] = 1
    c_grid[c[0]][c[1]] = 1
    
    #좀비바이러스 퍼짐
    for x, y in zombie_xy:       
        infect(c_grid, x, y)
        
    safe_zone = 0
    
    for i in range(N):
        for j in range(M):
            if c_grid[i][j] == 0:
                safe_zone += 1
                
    max_value = max(max_value, safe_zone)

print(max_value)
    
    