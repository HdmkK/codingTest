from collections import deque

def rotate_R(arr):

    tmp = arr[-1]

    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = tmp

def rotate_L(arr):

    tmp = arr[0]

    for i in range(len(arr)-1):
        arr[i] = arr[i+1]

    arr[-1] = tmp

def bfs(s_x, s_y):

    tmp = nums[s_x][s_y]
    count = 0

    queue = deque()
    queue.append((s_x, s_y))

    while queue:

        c_x, c_y = queue.popleft()
        nums[c_x][c_y] = -1
        count +=1

        for i in range(4):
            n_x = c_x + dx[i]
            n_y = c_y + dy[i]

            if (0<=n_x<m) and (0<=n_y<n) and nums[n_x][n_y] == tmp:
                queue.append((n_x, n_y))

    if count == 1:
        nums[s_x][s_y] = tmp
        return False
    
    return True

N, M, T = map(int, input().split())

nums = []

for i in range(N):
    nums.append(list(map(int, input().split())))

cmd = []

for i in range(T):
    cmd.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
m = N
n = M

for x, d, k in cmd:
    
    #원판 회전
    multiply = 0
    while True:

        multiply += 1

        if x * multiply > N:
            break

        idx = x*multiply-1

        for _ in range(k):
            if d == 0:
                rotate_R(nums[idx])
            elif d == 1:
                rotate_L(nums[idx])

    
    #인접한 숫자 제거(-1로 표시)
    #BFS?

    flag = False
    for x in range(m):
        for y in range(n):

            if nums[x][y] != -1:
                ret = bfs(x, y)

                if not flag:
                    flag = ret

    print(flag)
    if not flag:
        tmp = 0
        cnt = 0
        queue = []

        for i in range(N):
            for j in range(M):
                if nums[i][j] != -1:
                    tmp += nums[i][j]
                    queue.append((i, j))
        
        print(queue)
        if queue:
            v_mean = tmp / len(queue)
            print(v_mean)
            for i, j in queue:
                if nums[i][j] > v_mean:
                    nums[i][j] -= 1
                elif nums[i][j] < v_mean:
                    nums[i][j] += 1

    print(nums)


total = 0

for i in range(N):
    for j in range(M):
        if nums[i][j] != -1:
            total += nums[i][j]

print(total)

            
















    
    