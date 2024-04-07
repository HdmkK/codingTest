from collections import deque

# R, C = map(int, input().split())

dx = [0,0,1,-1]
dy = [1,-1,0,0]
board = []

def getCharIndex(c):
    return ord(c) - ord('A')

# for i in range(R):
#     board.append([])
#     tmp = input()
#     for c in tmp:
#         board[i].append(c)

R,C=map(int,input().split())
board=[list(input().rstrip()) for _ in range(R)]
        
#mem = {board[0][0]:-1}
#mem = {board[0][0]}
mem = [False for _ in range(26)]
mem[getCharIndex(board[0][0])] = True
 
        
def dfs(cur_x, cur_y, depth):
    
    max_depth = depth
    
    for i in range(4):
        next_x = cur_x + dx[i]
        next_y = cur_y + dy[i]
        
        if next_x >= 0 and next_x < R and next_y >= 0 and next_y < C:
            if not mem[getCharIndex(board[next_x][next_y])]:
                #mem[board[next_x][next_y]] = -1
                mem[getCharIndex(board[next_x][next_y])] = True
                ret = dfs(next_x, next_y, depth+1)
                mem[getCharIndex(board[next_x][next_y])] = False
                max_depth = max(max_depth, ret)
        
        
    return max_depth
    
    
    
print(dfs(0,0,1))
                
