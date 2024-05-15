N = int(input())



#N = A*B일 때, A와 B의 차이가 가장 작은 쌍을 구한다.


k = int(N**(1/2))
a = 0
b = 0
for i in range(k, 0, -1):
    if N % i == 0:
        a = i
        b = N//i
        break
    
print(a+b-2)
    

