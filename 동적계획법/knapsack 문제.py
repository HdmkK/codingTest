cargo = [
    (4,12),
    (2,1),
    (10,4),
    (1,1),
    (2,2)
]

capacity = 15


def knapsack(cargo, capacity):
    
    pack = [] #타뷸레이션을 위한 테이블

    for n in range(len(cargo)+1):
        
        pack.append([])
        
        for w in range(capacity+1):
            
            if n == 0 or w == 0:
                pack[n].append(0)
                
            if cargo[n-1][1] <= w:
                pack[n].append(max(pack[n-1][w], pack[n-1][w-cargo[n-1][1]] + cargo[n-1][0]))
            else:
                pack[n].append(pack[n-1][w])
                
    return pack[-1][-1]

print(knapsack(cargo, capacity))

        
    
    
    
    
    
    