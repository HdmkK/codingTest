import copy
from collections import deque


gear = []

gear1 = list(map(int, list(input())))
gear2 = list(map(int, list(input())))
gear3 = list(map(int, list(input())))
gear4 = list(map(int, list(input())))
gear.append(gear1)
gear.append(gear2)
gear.append(gear3)
gear.append(gear4)



turn_num = int(input())
turns = []
for _ in range(turn_num):
    turns.append(list(map(int, input().split())))
    
  
def right(gear):
    
    queue = deque(gear)
    tmp = queue.pop()
    queue.appendleft(tmp)
    return list(queue)

def left(gear):
    queue = deque(gear) 
    tmp = queue.popleft()
    queue.append(tmp)
    return list(queue)

def turning(gear_i, d):
    #시계방향
    if d == 1:
        ret = right(gear[gear_i])
        gear.pop(gear_i)
        gear.insert(gear_i, ret)
    #반시계방향
    elif d == -1:
        ret = left(gear[gear_i])
        gear.pop(gear_i)
        gear.insert(gear_i, ret)
        
    
            
    
for gear_i, d in turns:
    gear_i-=1
    
    check = [0, 0, 0, 0]
    check[gear_i] = d

    #오른쪽 나비효과
    k = gear_i
    t_d = d
    while k+1 <= 3:
        if gear[k][2] != gear[k+1][6]:
            t_d = -t_d
            check[k+1] = t_d
            k +=1
        else:
            break
    
    #왼쪽 나비효과
    k = gear_i
    t_d = d
    while k-1 >= 0:
        if gear[k][6] != gear[k-1][2]:
            t_d = -t_d
            check[k-1] = t_d
            k -=1
        else:
            break
        
    for i in range(4):
        if check[i] != 0:
            turning(i, check[i])

total = 0
for i in range(4):
      
    total += gear[i][0]*pow(2, i)
        
print(total)