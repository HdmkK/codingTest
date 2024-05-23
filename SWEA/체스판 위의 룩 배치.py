grid = []
for _ in range(8):
    grid.append(input())
    

row = {}
col = {}
count = 0
flag = True
for x in range(8):
    for y in range(8):
        if grid[x][y] == "O":
            count+=1
            if x in row or y in col:
                flag = False
                break
            else:
                row[x] = -1
                col[y] = -1
    
    if not flag:
        break

if count == 8 and flag:
    print("#{} yes".format(test_case))
else:
    print("#{} no".format(test_case))