N = int(input())

mem = []
for i in range(N):    
    tmp = list(map(int, input().split()))
    mem.append((tmp[0], tmp[1]))
    
max_value = 0

dp = {}


def dfs(n):
    
    if n == N:
        if mem[-1][0] == 1:
            return mem[-1][1]
        else:
            return 0
        
        
    
    yes = no = 0
    if n + mem[n-1][0] -1 <= N:
        yes = mem[n-1][1]
        if n + mem[n-1][0] <= N:
            if n+mem[n-1][0] not in dp:
                dp[n+mem[n-1][0]] = dfs(n+mem[n-1][0])
            yes += dp[n+mem[n-1][0]]
            
    if n+1 not in dp:
        dp[n+1] = dfs(n+1)
    no = dp[n+1]
    
    return max(yes, no)
     
        
    
print(dfs(1))