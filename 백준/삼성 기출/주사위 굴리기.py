N, M, s_x, s_y, command_num = map(int, input().split())

grid = []
for i in range(N):
    grid.append([])
    tmp = list(map(int, input().split()))
    for value in tmp:
        grid[i].append(value)

commands = []
for v in list(map(int, input().split())):
    commands.append(v-1)
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
############################################

#현재 주사위의 각 면에 있는 정수값을 저장
dice = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

#현재 Top에서의 동서남북에 있는 면의 번호
ewns_face = [3, 4, 2, 5]

c_x, c_y = s_x, s_y
c_top = 1

for i in commands:
    
    n_x = c_x + dx[i]
    n_y = c_y + dy[i]
    
    if (0 <= n_x < N and 0 <= n_y < M):
        
        #동으로 굴림
        if i == 0:
            c_top, ewns_face[0], ewns_face[1] \
                = ewns_face[1], c_top, 7-c_top, 
        
        #서로 굴림
        elif i == 1:
            c_top, ewns_face[0], ewns_face[1] \
                = ewns_face[0], 7-c_top, c_top
            
        #북으로 굴림
        elif i == 2: 
            c_top, ewns_face[2], ewns_face[3] \
                = ewns_face[3], c_top, 7-c_top
                
        #남으로 굴림
        elif i == 3:
            c_top, ewns_face[2], ewns_face[3] \
                = ewns_face[2], 7-c_top, c_top
                
        if grid[n_x][n_y] == 0:       
            grid[n_x][n_y] = dice[7-c_top]
            
        elif grid[n_x][n_y] != 0:
            dice[7-c_top] = grid[n_x][n_y]
            grid[n_x][n_y] = 0
        
        c_x, c_y = n_x, n_y
        print(dice[c_top])
            