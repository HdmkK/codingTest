from collections import deque

def solution(n, m, section):
    answer = 0
    
    
    count = 0 #칠한 횟수
    paint_s = 0 # paint_s 이전까지 칠함
    
    queue = deque(section)
    
    while queue and paint_s < n:
        
        idx = queue.popleft()
        idx-=1
        
        if idx < paint_s:
            continue
        
        if idx >= paint_s:
            count+=1
            paint_s = idx + m
            
            
    return count
        
        
        