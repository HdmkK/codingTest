start, end = map(int, input().split())


mem = []
n = 1
count = 0

while True:
    
    if count > 1001:
        break
    
    for _ in range(n):
        mem.append(n)
        count+=1
    n+=1
        
print(sum(mem[start-1: end]))
        
    
    