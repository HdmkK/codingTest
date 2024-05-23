S, T = input().split()


def gcd(n):
    
    answer = []
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer.append(i)
            
            if i**2 != n:
                answer.append(n//i)
    answer.sort()
    return answer

def lcm(n, m):
    
    for k in gcd(n*m):
        if k % n == 0 and k % m == 0:
            return k
        
k = lcm(len(S), len(T))
a = S*(k//len(S))
b = T*(k//len(T))

if a == b:
    print("yes")
else:
    print("no")
    