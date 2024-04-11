import copy

grid = []


for i in range(4):
    grid.append([])
    tmp = list(map(int, input().split()))
    for j in range(4):
        grid[i].append([tmp[j*2], tmp[j*2+1]-1])
        
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
max_value = 0

def solve(s_x, s_y, point, grid):
    
    global max_value
    
    #물고기 먹기
    s_d = grid[s_x][s_y][1]
    point+=grid[s_x][s_y][0]
    grid[s_x][s_y][0] = 0
    
    #물고기 이동
    for fish in range(1, 17):
        
        f_x = f_y = -1
        for i in range(4):
            for j in range(4):
                
                if fish == grid[i][j][0]:
                    f_x, f_y = i, j
                    break
            

        if f_x == -1 and f_y == -1:
            continue

        fd = grid[f_x][f_y][1]

        #이동할 수 있는 구역을 탐색
        for k in range(8):
            
            nd = (fd+k) % 8
            
            n_f_x = f_x + dx[nd]
            n_f_y = f_y + dy[nd]
            
            if not (0 <= n_f_x < 4 and 0 <= n_f_y < 4) or (n_f_x == s_x and n_f_y == s_y):
                continue
            
            grid[f_x][f_y][1] = nd
            grid[f_x][f_y], grid[n_f_x][n_f_y] =  grid[n_f_x][n_f_y], grid[f_x][f_y]
            break
            
    
    #상어가 다음에 먹을 물고기 탐색
    count=0
    for k in range(1, 4):
        
        n_s_x = s_x + dx[s_d]*k
        n_s_y = s_y + dy[s_d]*k
        
        if (0 <= n_s_x < 4 and 0 <= n_s_y < 4) and grid[n_s_x][n_s_y][0] > 0:
            count+=1 
            solve(n_s_x, n_s_y, point, copy.deepcopy(grid))
    
    #더 이상 먹을 물고기가 없다?
    if count == 0:
        global max_value
        max_value = max(max_value, point)

solve(0,0,0,grid[:])
print(max_value)
        