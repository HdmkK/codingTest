n = int(input())

d = []
mem = {}
for _ in range(n):
    d.append(int(input()))
  

def solve(n):
    
    if n == 1:
        return d[0]    
    elif n == 2:
        return d[0] + d[1]  
    elif n == 3:
        return max(d[0] + d[1], d[1] + d[2], d[2] + d[0])
    
    mem[0] = d[0]
    mem[1] = d[0] + d[1]
    mem[2] = max(d[0] + d[1], d[1] + d[2], d[2] + d[0])
    for i in range(3, n):
        mem[i] = max(mem[i-1], d[i] + mem[i-2], d[i] + d[i-1] + mem[i-3])
        
    return mem[n-1]

print(solve(n))
    
    
# #n번째에서 최대로 마실 수 있는 포도주량
# def dfs(n):
    
#     if n == 0:
#         mem[n] = d[0]
#         return mem[n]
#     elif n == 1:
#         mem[n] = d[0] + d[1]
#         return mem[n]
#     elif n == 2:
#         mem[n] = max(d[0]+d[1], d[1]+d[2], d[2]+d[0])
#         return mem[n]
    
#     mem[n] = max(dfs(n-1), d[n] + dfs(n-2), d[n] + d[n-1] + dfs(n-3))
#     return mem[n]
    

# print(dfs(n-1))