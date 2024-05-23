n, m = map(int, input().split())

def get_divisor(n):
    
    answer = []
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer.append(i)
            
            if i**2 != n:
                answer.append(n//i)
    answer.sort()
    return answer


lcm = 0
for k in get_divisor(n*m):
    if k % n == 0 and k % m == 0:
        lcm = k
        break
    
print(lcm)