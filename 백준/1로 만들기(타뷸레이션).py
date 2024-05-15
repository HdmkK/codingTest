N = int(input())


mem = {}
mem[1] = 0

for n in range(2, N+1):
    
    mem[n] = mem[n-1] + 1
    
    if n % 2 == 0:
        mem[n] = min(mem[n], mem[n//2]+1)
    if n % 3 == 0:
        mem[n] = min(mem[n], mem[n//3]+1)
        
print(mem[N])
        