import collections
import heapq

input_str = input().lower()

mem = collections.Counter(input_str)

heap = []


for key, value in mem.items():
    heapq.heappush(heap, (-value, key))
    

value, key = heapq.heappop(heap)
count = abs(value)

if len(mem) > 1:
    value2, key2 = heapq.heappop(heap)
    count2 = abs(value2)

    if count != count2:
        print(key.upper())
    else:
        print('?')
else:
    print(key.upper())
        

    
    