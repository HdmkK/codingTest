from collections import defaultdict


#소수 or 1 체크
def check(n):
    
    if n < 2:
        return True
    
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
        
    return True



A = int(input())


#B구하기

if check(A):
    #print(A)
    print("#{} {}".format(test_case, A))
else:
    #A를 소인수 분해
    mem = defaultdict(int)
    b = 1

    a = A
    for i in range(2, int(a**1/2)+1):
        
        while a % i == 0:
            a //= i
            mem[i] += 1
        
    for n, k in mem.items():   
        if k % 2 == 1:
            b *= n

    #print(b)
    print("#{} {}".format(test_case, b))