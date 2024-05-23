from collections import defaultdict

N, M = map(int, input().split())

edge = defaultdict(set)

count = 0
for _ in range(M):
    x, y = map(int, input().split())
    
    if x in edge and y in edge:
        ret = edge[x] & edge[y]
        if ret > 0:
            count += ret
            
    edge[x].add(y)
    edge[y].add(x)
   
    
print("#{} {}".format(test_case, count))
#print(count)
    