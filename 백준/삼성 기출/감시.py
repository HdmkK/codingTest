N, M = map(int, input().split())
grid = []
mem = {}
for i in range(N):
    grid.append([])
    tmp = list(map(int, input().split()))
    for j, v in enumerate(tmp):
        if (1 <= grid[i][j] <= 5):
            
            grid[i].append(v)
    
