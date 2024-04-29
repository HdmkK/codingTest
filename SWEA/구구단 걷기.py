N = int(input())


prev_a = 0
prev_b = 0

for a in range(1, N+1):
    
    if N % a == 0:
        b = N // a
        if a > b:
            print(prev_a + prev_b - 2)
            break
        prev_a = a
        prev_b = b
        
        
