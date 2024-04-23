N = int(input())

n = 1
mem = {}
while True:
    if N % n != 0:
        n+=1
        continue
    
    if int(N / n) in mem:
        break
    else:
        mem[n] = int(N / n)
    n+=1
        
print(mem)
answer = 10**12
for key, value in mem.items():
    answer = min (answer, key+value-2)
    
print(answer)
    
    
    