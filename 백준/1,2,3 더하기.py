N = int(input())

mem = {}

def dfs(n):
    
    if n == 1:
        mem[n] = 1
        return mem[n]
    if n == 2:
        mem[n] = 2
        return mem[n]
    if n == 3:
        mem[n] = 4
        return mem[n]
    
    if n-3 not in mem:
        mem[n-3] = dfs(n-3)
    if n-2 not in mem:
        mem[n-2] = dfs(n-2)
    if n-1 not in mem:
        mem[n-1] = dfs(n-1)
    return mem[n-3] + mem[n-2] + mem[n-1]
    
    

for _ in range(N):
    
    n = int(input())
    
    print(dfs(n))
    