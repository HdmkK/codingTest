import math

N = int(input())
position = []
for _ in range(N):
    position.append(list(map(int, input().split())))
    
point = 0
for i in range(N):
    
    x = position[i][0]
    y = position[i][1]
    
    d = math.sqrt(x**2 + y**2)
    
    ret = d // 20
    point += 10 - ret
    
print(int(point))
    