a, b = map(int, input().split())

a_divisor = []
b_divisor = []


def get_divisor(n):
    
    answer = []
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer.append(i)
            
            if i**2 != n:
                answer.append(n//i)
                
    answer.sort()
    return answer
result = set(get_divisor(a)) & set(get_divisor(b))
print(result)


