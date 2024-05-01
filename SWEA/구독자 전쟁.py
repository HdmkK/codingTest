N, A, B = map(int, input().split())

max = min(A, B)

min = (A+B) - N if (A + B) - N > 0 else 0

print(max, min)