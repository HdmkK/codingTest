n = int(input())

mem = {}
def dfs(n):
    
    if n == 1:
        mem[n] = 1
        return mem[n]
    elif n == 2:
        mem[n] = 2
        return mem[n]
    
    if n-2 not in mem:
        mem[n-2] = dfs(n-2)
    if n-1 not in mem:
        mem[n-1] = dfs(n-1)
    return mem[n-1] + mem[n-2]
    

print(dfs(n)%10007)