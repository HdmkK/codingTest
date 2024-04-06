import heapq

name = input()
candidates_num = int(input())
candidates = []
for _ in range(candidates_num):
    candidates.append(input())
    
heap = []
    
#각각의 팀명에 대해서
for i in range(candidates_num):
    
    #L구하기
    L = 0
    L += name.count('L')
    L += candidates[i].count('L')
    
    #O구하기
    O = 0
    O += name.count('O')
    O += candidates[i].count('O')
    
    #V구하기
    V = 0
    V += name.count('V')
    V += candidates[i].count('V')
    
    #E구하기
    E = 0
    E += name.count('E')
    E += candidates[i].count('E')
    
    probability = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    
    heapq.heappush(heap, (-probability, candidates[i]))
    

print(heapq.heappop(heap)[1])
    
    