A, B = map(int, input().split())

answer = 0

if A == B:
    answer = A
else:
    answer = 1
    
print(f"#{test_case} {answer}")