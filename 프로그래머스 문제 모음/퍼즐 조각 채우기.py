from collections import deque
import copy


#완
def find_block(board, f):
    m = len(board)
    n = len(board[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    result = []
    
    #BFS로 블럭단위로 좌표정보를 묶는다.
    for i in range(m):
        for j in range(n):
            if board[i][j] == f and not visited[i][j]:
                #print("hi")
                result.append([])
                queue = deque()
                
                queue.append((i,j))
                visited[i][j] = True
                
                while queue:
                    c_x, c_y = queue.popleft()
                    result[-1].append((c_x, c_y))
                    
                    for d in range(4):
                        n_x = c_x + dx[d]
                        n_y = c_y + dy[d]
                        
                        if (0 <= n_x < m) and (0 <= n_y < n):
                            if board[n_x][n_y] == f and not visited[n_x][n_y]:
                                visited[n_x][n_y] = True
                                queue.append((n_x, n_y))
                
    return result


def make_table(blocks):
    x_list, y_list = zip(*blocks)
    
    m = max(x_list) - min(x_list) + 1
    n = max(y_list) - min(y_list) + 1
    
    result = [[0 for _ in range(n)] for _ in range(m)]
    count = 0
    
    for x, y in blocks:
        x = x - min(x_list)
        y = y - min(y_list)
        result[x][y] = 1
        count+=1
    
    return result, count

def rotate_90(table):
    result = list(map(list, zip(*table[::-1])))
    return result
    
def rotate_180(table):
    result = [ t[::-1] for t in table[::-1]]
    return result

def rotate_270(table):
    result = list(map(list, zip(*table)))[::-1]
    return result
                    

def solution(game_board, table):
    answer = -1
    total = 0
    
    #game_board, table 각각 빈자리, 퍼즐을 좌표정보로 변환
    empty_blocks = find_block(game_board, 0)
    blocks = find_block(table, 1)
    
    
    #각각의 빈공간에 대해서 퍼즐을 차례대로 회전하면서 맞춰본다.
    for e in empty_blocks:
        empty_table, _ = make_table(e)
        
        for idx, p in enumerate(blocks):
                
            pt_0, count = make_table(p)
            
            if pt_0 == empty_table:
                blocks.pop(idx)#블럭사용했으니 제외
                total += count
                break
            
            pt_90 = rotate_90(pt_0)
            if pt_90 == empty_table:
                blocks.pop(idx)#블럭사용했으니 제외
                total += count
                break
                
            pt_180 = rotate_180(pt_0)
            if pt_180 == empty_table:
                blocks.pop(idx)#블럭사용했으니 제외
                total += count
                break
                
            pt_270 = rotate_270(pt_0)
            if pt_270 == empty_table:
                blocks.pop(idx)#블럭사용했으니 제외
                total += count
                break
            
                
        
    
    return total