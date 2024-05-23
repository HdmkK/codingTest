N, M = map(int, input().split())

# 1 -> 흑
# 2 -> 백
event = []
for _ in range(M):
    x, y, who = map(int, input().split())
    event.append((x-1, y-1, who))
    
    
grid = []
for x in range(N):
    grid.append([])
    for y in range(N):
        if 