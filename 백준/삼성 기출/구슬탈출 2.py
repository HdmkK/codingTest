from collections import deque


def solve():
    
    m, n = tuple(map(int, input().split()))

    mem = []

    # 동 : i=0
    # 서 : i=1
    # 남 : i=2
    # 북 : i=3
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    #탐색한 적이 있는 상태(레드위치, 블루위치)는 다시 탐색하지 않기 위해 표시
    visited = {}
    red_start_x = red_start_y = 0
    blue_start_x = blue_start_y = 0

    for i in range(m):
        mem.append([])
        row = input()
        for j, r in enumerate(row):
            if r == 'R':
                red_start_x = i
                red_start_y = j
            elif r == 'B':
                blue_start_x = i
                blue_start_y = j
                
            mem[i].append(r)
            
            
    queue = deque()
    #(레드 시작점, 블루 시작점, 깊이=0)
    queue.append((red_start_x, red_start_y, blue_start_x, blue_start_y, 0))
    
    while queue:
        cur_red_x, cur_red_y, cur_blue_x, cur_blue_y, depth = queue.popleft()
        
        if depth > 10:
            print(-1)
            return
        elif mem[cur_red_x][cur_red_y] == 'O':
            print(depth)
            return
        
        #RED, BLUE 모두 동서남북 탐색
        for i in range(4):
            
            next_red_x, next_red_y = cur_red_x, cur_red_y
            while True:
                next_red_x += dx[i]
                next_red_y += dy[i]
                
                if next_red_x >= 0 and next_red_x < m and next_red_y >= 0 and next_red_y < n:
                    if mem[next_red_x][next_red_y] == '.':
                        continue
                    elif mem[next_red_x][next_red_y] == '#':
                        next_red_x -= dx[i]
                        next_red_y -= dy[i]
                        break
                    elif mem[next_red_x][next_red_y] == 'O':
                        break
                    
            next_blue_x, next_blue_y = cur_blue_x, cur_blue_y
            while True:
                next_blue_x += dx[i]
                next_blue_y += dy[i]
                
                if next_blue_x >= 0 and next_blue_x < m and next_blue_y >= 0 and next_blue_y < n:
                    if mem[next_blue_x][next_blue_y] == '.':
                        continue
                    elif mem[next_blue_x][next_blue_y] == '#':
                        next_blue_x -= dx[i]
                        next_blue_y -= dy[i]
                        break
                    elif mem[next_blue_x][next_blue_y] == 'O':
                        break
                
            #RED와 BLUE의 위치가 같아질 경우를 고려
            #동일한 방향으로 움직일때 더 많은 거리를 움직인 공이 나중에 해당 위치로 온 것이므로, 백스텝
            
            if next_red_x == next_blue_x and next_red_y == next_blue_y and mem[next_red_x][next_blue_y] != 'O':
                if (abs(next_red_x - cur_red_x) + abs(next_red_y - cur_red_y)) > \
                    (abs(next_blue_x - cur_blue_x) + abs(next_blue_y - cur_blue_y)):
                    next_red_x -= dx[i]
                    next_red_y -= dy[i]
                else:
                    next_blue_x -= dx[i]
                    next_blue_y -= dy[i]
                
            #어떤 경우에 큐에 넣을까?
            #BLUE가 골인한 경우 외에는 모두 고려해야 하므로 큐에 삽입
            if (next_red_x, next_red_y, next_blue_x, next_blue_y) not in visited and mem[next_blue_x][next_blue_y] != 'O':
                visited[(next_red_x, next_red_y, next_blue_x, next_blue_y)] = -1
                queue.append((next_red_x, next_red_y, next_blue_x, next_blue_y, depth+1))
                
    print(-1)
                           

solve()