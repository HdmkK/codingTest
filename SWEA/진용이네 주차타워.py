from collections import deque
import heapq

n, m = map(int, input().split())

price_per_kg = []
for _ in range(n):
    price_per_kg.append(int(input()))
    
car_weight = []
for _ in range(m):
    car_weight.append(int(input()))
   
#이벤트를 차례로 꺼내올 큐 
event = deque()
for _ in range(m*2):
    event.append(int(input()))
    
#빈 주차공간을 저장할 힙
heap = []
for i in range(n):
    heapq.heappush(heap, i)
    
#현재 차량이 어느 주차칸에 있는지 저장할 딕셔너리
parking_where = {}
    
#차량 대기 큐
wait_queue = deque()

#누적 비용
total_cost = 0
    
while event:
    
    value = event.popleft()
    
    #차가 들어온다면
    if value > 0:
        value -= 1
        wait_queue.append(value) #줄세우기
    #차가 들어온다면
    elif value < 0:
        value = -value - 1
        park_lot = parking_where[value]
        parking_where[value] = -1
        heapq.heappush(heap, park_lot)
        
    #주차 작업 수행
    #대기 차가 있고 빈 주차공간이 있다면
    if wait_queue and heap:
        car = wait_queue.popleft()
        park_lot = heapq.heappop(heap)
        
        parking_where[car] = park_lot
        
        #비용 = 차량무게 X 주차공간 책정 가격
        cost = car_weight[car] * price_per_kg[park_lot]
        total_cost += cost
        

print(total_cost)
        
        
        
        
    


