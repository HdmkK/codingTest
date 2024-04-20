T = int(input())

for _ in range(T):
    
    a, b, c = map(int, input().split())
    err = False
    count = 0
    
    while b >= c:
            
        count+=1
        b-=1
        
    while a >= b:
    
        count+=1
        a-=1
        
    if a <= 0:
        print(f"")
    else:
        print(count)
        
    