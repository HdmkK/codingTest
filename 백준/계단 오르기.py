stair_num = int(input())

stairs = []

for _ in range(stair_num):
    stairs.append(int(input()))


mem = {}

#cur까지의 (max_profit, 1step count)를 반환


def solve(cur):
    
    if cur == 0:
        mem[0] = stairs[0]
        return mem[0]
    elif cur == 1:
        mem[1] = stairs[0] + stairs[1]
        return mem[1]
    elif cur == 2:
        mem[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
        return mem[2]
    
    
    if cur-2 not in mem:
        mem[cur-2] = solve(cur-2)
    if cur-3 not in mem:
        mem[cur-3] = solve(cur-3)
        
    return max(mem[cur-2] +  stairs[cur], mem[cur-3] + stairs[cur-1] + stairs[cur])
    
   
   
print(solve(stair_num-1))