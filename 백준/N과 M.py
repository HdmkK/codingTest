N, M = map(int, input().split())

nums = [n for n in range(1, N+1)]
mem = {}

answer = []

def solve(curr):
    
    if len(curr) == M:
        #answer.append(curr[:])
        print(*curr)
        return
    
    for i in range(N):
        if i not in mem:
            curr.append(nums[i])
            mem[i] = -1
            solve(curr)
            curr.pop()
            del mem[i] 


solve([])

