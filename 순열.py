nums = [1, 2, 3, 4]

answer = []

mem = {}

def dfs(cur):
    
    if len(cur) == len(nums):
        answer.append(cur[:])
        return
    
    
    for n in nums:
        #if n not in cur:
        if n not in mem:
            mem[n] = -1
            cur.append(n)
            dfs(cur)
            del mem[n]
            cur.pop()

dfs([])
print(answer)