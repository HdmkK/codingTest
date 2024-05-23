N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
    
tels = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], \
    [(1,0), (2,0), (2,1)], [(0,1), (0,2), (-1,2)],[(-1,0), (-2,0), (-2,-1)], [(0,-1), (0,-2), (1,-2)], \
        [(1,0), (2,0), (2,-1)], [(0,1), (0,2), (1,2)],[(-1,0), (-2,0), (-2,1)], [(0,-1), (0,-2), (-1,-2)], \
            [(1,0), (0,1), (1,1)], \
                [(1,0), (1,1), (2,1)], [(0,1), (-1,1), (-1,2)], \
                    [(1,0), (1,-1), (2, -1)], [(0,1), (1,1), (1,2)], \
                        [(0,1), (0,2), (1,1)], [(-1,0), (-1,1) ,(-2,0)], [(0,-1), (-1,-1), (0,-2)], [(1,0), (2,0), (1,-1)]]

max_v = 0


for x in range(N):
    for y in range(M):
           
        for tel in tels: #기준 grid[x][y]에 대해서 모든 패턴 고려
            #print(tel)
            flag = False
            sum = grid[x][y]
            for block in tel:
                n_x = x + block[0]
                n_y = y + block[1]
                
                if (0<=n_x<N)and(0<=n_y<M):
                    sum+=grid[n_x][n_y]
                else:
                    flag = True
                    break
            
            if flag:
                continue
            else:
                max_v = max(max_v, sum)
                

print(max_v)