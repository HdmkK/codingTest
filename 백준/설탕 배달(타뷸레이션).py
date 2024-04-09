N = int(input())


mem = []

for w in range(N+1):
    
    if w < 6:
        if w == 3 or w== 5:
            mem.append(1)
        else:
            mem.append(0)
        continue
    
    if mem[w-3] == 0 and mem[w-5] == 0:
        mem.append(0)
    elif mem[w-3] == 0 or mem[w-5] == 0:
        mem.append(mem[w-3]+1 if mem[w-3] != 0 else mem[w-5]+1)
    else:
        mem.append(min(mem[w-3], mem[w-5])+1)
        
if mem[-1] == 0:
    print(-1)
else:
    print(mem[-1])
    



   

