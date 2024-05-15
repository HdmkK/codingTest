nums = [4,9,7,5,1]
target = 15
n = len(nums)
answer = []


def dfs(cur, start):
    
    if len(cur) == 3:
        if sum(cur) == target:
            answer.append(cur[:])
            return
    
    for i in range(start, n):
        cur.append(nums[i])
        dfs(cur, i+1)
        cur.pop()
    
dfs([], 0)
print(answer)