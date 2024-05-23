from collections import deque



def check(n):
    
    s = deque(str(n))
    
    while len(s) > 1:
        if s.popleft() != s.pop():
            return False
        
    return True

A, B = map(int, input().split())

count = 0
for n in range(A, B+1):
    
    if check(n):
        a = int(n**(1/2))
        if a**2 == n:
            if check(a):
                count+=1

print("#{} {}".format(test_case, count))