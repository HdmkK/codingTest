N = int(input())

mem = []
for i in range(N):    
    tmp = list(map(int, input().split()))
    mem.append((tmp[0], tmp[1]))
    
max_value = 0

dp = {}

n = N
while n > 0:
    
    if n == N:
        if mem[-1][0] == 1:
            dp[n] = mem[-1][1]
        else:
            dp[n] = 0
        n-=1
        continue
    
    yes = no = 0
    #상담 할 때 -> 조건에 맞으면 고려
    if n + mem[n-1][0] - 1 <= N:
        yes = mem[n-1][1]
        if n+mem[n-1][0] <= N:
            yes +=dp[n+mem[n-1][0]]
    
    
    #상담 안할 때 -> 이전 단계의 최댓값을 그대로 가져옴
    no = dp[n+1]
    
    #둘중 더 큰 값을 채택
    dp[n] = max(yes, no)
    
    n-=1
    
print(dp[1])