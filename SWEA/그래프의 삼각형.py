from collections import defaultdict

N, M = map(int, input().split())

mem = defaultdict(list)
edge = []
for _ in range(M):
    x, y = map(int, input().split())
    mem[x].append(y)
    edge.append((x, y))
    


for x, y in edge:
    
    for n in mem[x]:
        if 
    