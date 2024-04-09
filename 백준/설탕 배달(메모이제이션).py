import sys
sys.setrecursionlimit(100000)

N = int(input())


mem = {}

def solve(cur):
   
    if cur < 0:
        return -1
    elif cur == 0:
        return 0
    
    
    if cur-3 not in mem:
        mem[cur-3] = solve(cur-3)
        
    if cur-5 not in mem:
        mem[cur-5] = solve(cur-5)
    
    if mem[cur-3] == -1 and mem[cur-5] == -1:
        return -1
    elif mem[cur-3] == -1 or mem[cur-5] == -1:
        return mem[cur-3] + 1 if mem[cur-3] != -1 else mem[cur-5] + 1
    else:
            return min(mem[cur-3], mem[cur-5]) + 1

ret = solve(N)

if not ret:
    print(-1)
else:
    print(ret)
   
   