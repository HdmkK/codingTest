from collections import deque

def solution(maps):
    answer = 0
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    width = len(maps)
    height = len(maps[0])
    
    queue = deque()
    queue.append((0,0,1))
    
    while queue:
        cur_x, cur_y, depth = queue.popleft()
        
        if cur_x == width-1 and cur_y == height-1:
            return depth
        
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if next_x >= 0 and next_x < width and next_y >= 0 and next_y < height:
                if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] = 0
                    queue.append((next_x, next_y, depth+1))
                    
    return -1