N = int(input())

k = 1
sum = 0

while True:
    if N <= k:
        break
    
    num = N * k + k
    sum += num
    k+=1
    

print(sum)