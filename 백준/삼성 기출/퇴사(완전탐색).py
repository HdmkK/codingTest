

N = int(input())

mem = []
for i in range(N):    
    tmp = list(map(int, input().split()))
    mem.append((tmp[0], tmp[1]))
    
max_value = 0
    
#until : 해당 날까지 상담불가
def backtracking(cur, n):
    
    if n > N:
        global max_value
        max_value = max(max_value, sum(cur))
        return
    
    
    time, profit = mem[n-1]
    #상담한다면
    if (n + time - 1) <= N:
        cur.append(profit)
        backtracking(cur, n+time)
        cur.pop()
    
    #상담안한다면
    backtracking(cur, n+1)

backtracking([], 1)
print(max_value)
    

    


    
    

    