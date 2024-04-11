import copy

N = int(input())
max_value = 0

grid = []
for i in range(N):
    grid.append([])
    tmp = list(map(int, input().split()))
    for value in tmp:
        max_value = max(max_value, value)
        grid[i].append(value)
        
 

#동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
        
        
def action(c_x, c_y, d, grid):
    global max_value
    
    if not (0 <= c_x < N and 0 <= c_y < N):
        return
    
    #흡수하고
    k = 0
    while True:
        k += 1
        b_x = c_x + dx[(d+2)%4]*k
        b_y = c_y + dy[(d+2)%4]*k
        
        if (0 <= b_x < N and 0 <= b_y < N):
            if grid[b_x][b_y] == grid[c_x][c_y]:
                grid[c_x][c_y] += grid[b_x][b_y]
                max_value = max(max_value, grid[c_x][c_y])         
                grid[b_x][b_y] = 0
                break
            elif grid[b_x][b_y] == 0:
                continue
        break
    
        
                
    #이동
    while True:
        n_x = c_x + dx[d]
        n_y = c_y + dy[d]
        
        if (0 <= n_x < N and 0 <= n_y < N):
            if grid[n_x][n_y] == 0:
                grid[c_x][c_y], grid[n_x][n_y] = grid[n_x][n_y], grid[c_x][c_y]
                c_x, c_y = n_x, n_y
                continue
        break
    
    
count = 0
def solve(grid, count):
    
    for d in range(4):
        
        if d == 0:#동
            cp_grid = copy.deepcopy(grid)
            for c_y in range(N-1,-1,-1):
                for c_x in range(N):      
                    action(c_x, c_y, d, cp_grid)
            if count < 5:
                solve(copy.deepcopy(cp_grid), count+1)                     
        elif d == 1:#남
            cp_grid = copy.deepcopy(grid)
            for c_x in range(N-1,-1,-1):
                for c_y in range(N):
                    action(c_x, c_y, d, cp_grid)
            if count < 5:
                solve(copy.deepcopy(cp_grid), count+1)
        elif d == 2:#서
            cp_grid = copy.deepcopy(grid)
            for c_y in range(N):
                for c_x in range(N):
                    action(c_x, c_y, d, cp_grid)
            if count < 5:
                solve(copy.deepcopy(cp_grid), count+1)
        elif d == 3:#북       
            cp_grid = copy.deepcopy(grid)
            for c_x in range(N):
                for c_y in range(N):
                    action(c_x, c_y, d, cp_grid)
    
            if count < 5:
                solve(copy.deepcopy(cp_grid), count+1)
        
                                                
solve(grid, 1)
print(max_value)
        