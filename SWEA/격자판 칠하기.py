import copy



def check(c_grid, cur_color):
    
    flag = True
    for x in range(N):
        for y in range(M):
           
            if c_grid[x][y] != "?":
                if c_grid[x][y] != cur_color:
                    flag = False
                    break
                
            if cur_color == "#":
                cur_color = "."
            else:
                cur_color = "#"
                
        if not flag:
            break
        
        if M % 2 == 0:
            if cur_color == "#":
                cur_color = "."
            else:
                cur_color = "#"
        
    return flag


N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(input()))
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    

c_grid = copy.deepcopy(grid)
ret1 = check(c_grid, "#")
c_grid = copy.deepcopy(grid)
ret2 = check(c_grid, ".")

if ret1 or ret2:
    print("possible")
else:
    print("impossible")
    

