class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        answer = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        width = len(grid[0])
        height = len(grid)

        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        #탐색 재귀
        def dfs(cur_x,cur_y):

            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]

                if next_x >= 0 and next_x < height and next_y >= 0 and next_y < width: # 방문X, 다음에 방문할 지역이 범위 내
                    if not visited[next_x][next_y] and grid[next_x][next_y] == "1": #그 곳이 땅이라면
                        visited[next_x][next_y] = True
                        dfs(next_x, next_y)





        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1" and not visited[i][j]: #방문하지 않은 땅이라면
                    visited[i][j] = True
                    answer+=1
                    dfs(i,j)


        return answer