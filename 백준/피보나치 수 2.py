N = int(input())


mem = {}

def dfs(n):
    
    if n == 0:
        mem[0] = 0
        return mem[0]
    elif n == 1:
        mem[1] = 1
        return mem[1]
    
    if n-1 not in mem:
        mem[n-1] = dfs(n-1)
    if n-2 not in mem:
        mem[n-2] = dfs(n-2)
    return mem[n-1] + mem[n-2]

print(dfs(N))