from collections import deque

N = int(input())
apples_num = int(input())

apples = []
for _ in range(apples_num):
    
    tmp = list(map(int, input().split()))
    apples.append([tmp[0]-1, tmp[1]-1])


command_num = int(input())

commands = {}
for _ in range(command_num):
    tmp = input().split()
    commands[int(tmp[0])] = tmp[1]
    
seconds = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
c_x = c_y = 0
c_d = 0
# 0: 동, 1: 남, 2: 서, 3: 북

snake_queue = deque()
snake_queue.append([0,0])

while True:
    
    
    seconds+=1
         
    n_x = c_x + dx[c_d]
    n_y = c_y + dy[c_d]
    c_x = n_x
    c_y = n_y
    
    if not (0 <= n_x < N and 0<= n_y < N) or ([n_x, n_y] in snake_queue):
        break
    
    if [n_x, n_y] in apples:
        snake_queue.append([n_x, n_y])
        apples.remove([n_x, n_y])
    else:
        snake_queue.append([n_x, n_y])
        snake_queue.popleft()
    
    if seconds in commands:
        if commands[seconds] == 'D':
            c_d = (c_d + 1)%4
        elif commands[seconds] == 'L':
            c_d = (c_d - 1)
            if c_d < 0:
                c_d = 3
                
print(seconds)
        
        
    
    