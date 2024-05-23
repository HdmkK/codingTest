from math import sqrt

N = int(input())

answer = []

for i in range(1, int(sqrt(N))+1):
    if N % i == 0:
        answer.append(i)
        
        if i*i != N:
            answer.append(N//i)
            
answer.sort()
tmp = " ".join(map(str, answer))
print(tmp)