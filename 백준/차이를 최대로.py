N = int(input())

nums = list(map(int, input().split()))



#일단 배열을 주면 계산하는 함수를 만들자

def cal(nums):
    
    sum = 0
    for i in range(N-1):
        sum += abs(nums[i]-nums[i+1])
    return sum

mem = {}
max_value = 0

def dfs(curr):
    
    if len(curr) == N:
        global max_value
        max_value = max(max_value, cal(curr))
        return
    
    for i in range(N):
        if i not in mem:
            curr.append(nums[i])
            mem[i] = -1
            dfs(curr)
            curr.pop()
            del mem[i]


dfs([])
print(max_value)

