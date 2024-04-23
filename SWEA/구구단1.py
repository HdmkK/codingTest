N = int(input())

answer = "No"
for k in range(1, 10):
    ret = N / k
    
    if int(ret) == ret and ret % 10 == ret and ret != 0:
        answer = "Yes"
        break

print(answer)