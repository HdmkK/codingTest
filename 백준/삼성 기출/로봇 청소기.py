R, C = map(int, input().split())
s_x, s_y, s_d = map(int, input().split())

grid = []
for i in range(R):
    grid.append([])
    tmp = list(map(int, input().split()))
    for value in tmp:
        grid[i].append(value)
  
count = 0

# 0:북, 1:동, 2:남, 3:서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0 -> 청소X
# -1 -> 청소O
# 1 -> 벽
def search(c_x, c_y, c_d):
    #c_x, c_y는 반드시 청소O or 청소X
    global count
        
    while True:
        
        #현재칸이 청소X -> 청소
        if grid[c_x][c_y] == 0:         
            count+=1          
            grid[c_x][c_y] = -1
        
        flag = False
        for i in range(4):
            
            n_x = c_x + dx[i]
            n_y = c_y + dy[i]
            
            #유효칸에서 청소되지 않은 칸을 하나라도 발견한다면
            if (0 <= n_x < R and 0 <= n_y < C):
                if grid[n_x][n_y] == 0:
                    flag = True
                    break
                
        #청소 안된 곳O
        if flag:
            c_d = c_d - 1
            if c_d < 0:
                c_d = 3
                
            n_x = c_x + dx[c_d]
            n_y = c_y + dy[c_d]
            
            if (0 <= n_x < R and 0 <= n_y < C):
                if (grid[n_x][n_y] == 0):                   
                    c_x, c_y = n_x, n_y
            continue
        else:
            #바라보는 방향 기준으로 뒤로 갈수 있는지
            back_x = c_x + dx[(c_d+2)%4]
            back_y = c_y + dy[(c_d+2)%4]
        
            if (0 <= back_x < R and 0 <= back_y < C):
                if grid[back_x][back_y] != 1:#뒤로 갈 수 있다면
                    c_x, c_y = back_x, back_y
                    continue
            break        
            
                    
            
search(s_x, s_y, s_d)
print(count)

            
        
            
            
    
        
            
            
            
            
                
        
        
    
        
    
        
    

