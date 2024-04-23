import heapq
import math
N = int(input())
grid = []

for i in range(N):
    grid.append([])
    tmp = input()
    for c in tmp:
        grid[i].append(c)
        
#mem = {}
heap = []
answer = True
sq_n = 0

for x in range(N):
    for y in range(N):
        
        if grid[x][y] == "#":
            #mem[(x, y)] = -1
            heapq.heappush(heap, (x, y))
            

s_x, s_y = heapq.heappop(heap)

k = math.sqrt(len(heap)+1)
if int(k) != k:
    answer = False
    print(s_x, s_y)
else:
    sq_n = int(k)
    
for x in range(sq_n):
    for y in range(sq_n):
        
        c_x = s_x + x
        c_y = s_y + y
         
        if grid[c_x][c_y] != "#":
            answer = False
            
if answer:
    print("YES")
else:
    print("NO")

        
        
    
        
                   
            
                
            