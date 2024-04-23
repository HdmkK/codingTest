N, K = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
answer = a[-1] - a[0]

for i in range(N):
    if i + K - 1 > N - 1:
        break
    answer = min(answer, a[i+K-1]-a[i])
    
print(answer)
    
    