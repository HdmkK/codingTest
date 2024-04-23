TC = int(input())

N = int(input())
num = list(map(int, input().split()))

sum_list = []
max_v = 0

for i in range(N):
    if i == 0:
        if num[0] < 0:
            sum_list.append(0)
        else:
            sum_list.append(num[0])
        max_v = max(max_v, sum_list[0])
        continue
    
    sum = num[i-1] + num[i]
    if sum < 0:
        sum_list.append(0)
    else:
        sum_list.append(sum_list[i-1] + num[i])
    
    max_v = max(max_v, sum_list[i])
print(sum_list)
print(max_v)
        