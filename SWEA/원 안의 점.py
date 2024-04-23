T = int(input())


N = int(input())

count = 0
for x in range(1, N):
    for y in range(1, N):
        if x**2+y**2 <= N**2:
            count+=1
            

answer = 1 + 4 * ( N + count)
print(f"#{test_case} {answer}")
        

