
    
#해당 방향으로 5개 이상 O이 있는지 체크 -> boolean
def check(x, y, i):
    
    answer = False
    for k in range(1, 5):
        n_x = x + dx[i]*k
        n_y = y + dy[i]*k
        
        if (0 <= n_x < N) and (0 <= n_y < N):
            if grid[n_x][n_y] == "o":
                
                if k == 4:
                    answer = True
                continue
        break
    return answer
    

N = int(input())
grid = []

for _ in range(N):
    grid.append(list(input()))
    
dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]
    
            
answer = False   
for x in range(N):
    for y in range(N):
        
        if grid[x][y] == "o":
            for i in range(8):
                if check(x, y, i):
                    answer = True
                    break
                
        if answer:
            break
    if answer:
        break
    
if answer:
    print("#{} YES".format(test_case))
else:
    print("#{} NO".format(test_case))