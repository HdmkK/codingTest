import random
import math



#소수인지 check
def check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return True
    return False
    
n = int(input())

while True:
    
    x = random.randint(2, 10**7)
    if not check(x):
        continue
    
    y = x - n
    if not check(y):
        continue
    
    print(x, y)
    break

    