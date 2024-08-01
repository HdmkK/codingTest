from collections import deque
import heapq

def get_shark_xy():
    for x in range(N):
        for y in range(N):
            if board[x][y] == 9:
                board[x][y] = 0
                return (x, y)
            
def find_next_fish()->tuple:
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    target_list = []
    queue.append((cur_shark_x, cur_shark_y, 0))
    visited[cur_shark_x][cur_shark_y] = True
    target_depth = 0
    
    
    while queue:

        c_x, c_y, depth = queue.popleft()

        if (0 < target_depth < depth):
            return (target_list, target_depth)

        if (0 < board[c_x][c_y] < cur_shark_size):
                target_list.append((c_x, c_y))
                target_depth = depth
            
        for i in range(4):
            n_x = c_x + dx[i]
            n_y = c_y + dy[i]

            if (0<=n_x<N) and (0<=n_y<N):
                if not visited[n_x][n_y] and not (board[n_x][n_y] > cur_shark_size):
                    visited[n_x][n_y] = True
                    queue.append((n_x, n_y, depth+1))
    
    return (target_list, target_depth)
        
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

cur_shark_x, cur_shark_y = get_shark_xy()
cur_shark_size = 2
time = eat_cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while True:
    t_list, t_depth = find_next_fish()
    if len(t_list)==0:
        break
    
    t_list.sort()
    cur_shark_x, cur_shark_y = t_list[0]
    board[cur_shark_x][cur_shark_y] = 0
    eat_cnt+=1
    if eat_cnt == cur_shark_size:
        cur_shark_size+=1
        eat_cnt=0
    time+=t_depth


print(time)