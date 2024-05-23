n = int(input())
schedule = list(map(int, input().split()))


mem = []
for i in range(7):
    if schedule[i] == 1:
        mem.append(i)
        
min_v = None
flag = True
for start in mem:
    i = start
    count = 0
    k = n
    while k > 0:
        if schedule[i] == 1:
            k -=1
        count += 1
        i = (i+1) % 7
    
    if flag:
        min_v = count
        flag = False
    else:
        min_v = min(min_v, count)
    
print("#{} {}".format(test_case, min_v))
        
    


    
    