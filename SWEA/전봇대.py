N = int(input())

mem = []
count = 0

for _ in range(N):
    A, B = map(int, input().split())
    
    if mem:
        for p_a, p_b in mem:
            if (p_a < A and p_b > B) or (p_a > A and p_b < B):
                count += 1

    mem.append((A, B))
                
print(count)
                
    