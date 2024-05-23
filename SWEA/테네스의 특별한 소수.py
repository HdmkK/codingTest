def get_primes(n, a):
    
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        
        for j in range(i*i, n+1, i):
            arr[j] = 0
            
    if a < 2:
        a = 2
    return [i for i in arr[a:] if arr[i]]

D, A, B = map(int, input().split())

count = 0
p = get_primes(B, A)
for n in p:
    if str(D) in str(n):
        count+=1
print(count)