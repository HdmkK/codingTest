import collections
import heapq
import copy

N = int(input())

string = str(N)

mem = collections.defaultdict(int)
heap = []
for c in string:
    c = int(c)
    heapq.heappush(heap, -c)
    mem[c] += 1
    
max_v = ""
while heap:
    num = heapq.heappop(heap)
    num = str(-num)
    max_v += num

max_v = int(max_v)

k = 2
flag = False
while N*k <= max_v:
    c_mem = copy.deepcopy(mem)
    
    for c in str(N*k):
        c = int(c)
        if c in c_mem:
            c_mem[c] -=1
            
            if c_mem[c] == 0:
                del c_mem[c]
        else:
            break
    
    if len(c_mem) == 0:
        flag = True
        print(N*k)
        break
    else:
        k+=1
        continue
    
if flag:
    print("possible")
else:
    print("impossible")
