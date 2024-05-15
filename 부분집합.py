nums = [1,2,3,4]
n = len(nums)
answer = []

def dfs(cur, start):
    
    if len(cur) == k:
        answer.append(cur[:])
        return
    
    for i in range(start, n):
        cur.append(nums[i])
        dfs(cur, i+1)
        cur.pop()
    
    


for k in range(n+1):
    dfs([], 0)
    
print(answer)