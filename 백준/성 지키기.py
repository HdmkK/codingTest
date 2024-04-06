m, n = map(int, input().split())

mem = []

for i in range(m):
    mem.append([])
    tmp = input()
    for c in tmp:
        mem[i].append(c)
    
row_count = 0    
for i in range(m):
    for j in range(n):
        if mem[i][j] != '.':
            break
        if j == n-1:
            row_count+=1
            
col_count = 0
for j in range(n):
    for i in range(m):
        if mem[i][j] != '.':
            break
        if i == m-1:
            col_count+=1
            
            
print(max(row_count, col_count))
    
    
        