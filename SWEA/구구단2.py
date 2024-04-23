A, B = map(int, input().split())

if (A % 10 != A) or (B % 10 != B):
    print(-1)
else:
    print(A*B)