import sys
sys.setrecursionlimit(10**6)

K = int(input())

drinks = []
for _ in range(K):
    drinks.append(int(input()))
    

mem = {}

def solve(n):
    
    if n == 0:
        mem[0] = drinks[0]
        return mem[0]
    elif n == 1:
        mem[1] = drinks[0] + drinks[1]
        return mem[1]
    elif n == 2:
        mem[2] = max(drinks[0] + drinks[1], drinks[1] + drinks[2], drinks[2] + drinks[0])
        return mem[2]
    
    if n-1 not in mem:
        mem[n-1] = solve(n-1)
    if n-2 not in mem:
        mem[n-2] = solve(n-2)
    if n-3 not in mem:
        mem[n-3] = solve(n-3)
    
    
    return max(mem[n-2] + drinks[n], mem[n-3] + drinks[n-1] + drinks[n], mem[n-1])

print(solve(K-1))
    