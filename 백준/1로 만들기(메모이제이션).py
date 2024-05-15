import sys
sys.setrecursionlimit(10**6)

N = int(input())

mem = {}


def dfs(n):
    
    if n == 1:
        mem[n] = 0
        return mem[n]
    
    if n-1 not in mem:
        mem[n-1] = dfs(n-1)
    mem[n] = mem[n-1] + 1
    
    if n % 2 == 0:
        if n//2 not in mem:
            mem[n//2] = dfs(n//2)
        mem[n] = min(mem[n], mem[n//2]+1)
    if n % 3 == 0:
        if n//3 not in mem:
            mem[n//3] = dfs(n//3)
        mem[n] = min(mem[n], mem[n//3]+1)
    
    return mem[n]
    

print(dfs(N))
    
    