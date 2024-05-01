N = int(input())

earn = list(map(int, input().split()))

avg = sum(earn)/N
count = 0

for e in earn:
    if e <= avg:
        count += 1

print(count)