sequence_length = int(input())

nums = list(map(int, input().split()))

answer = [-1 for _ in range(sequence_length)]
stack = []

for i, num in enumerate(nums):
    
    while stack and stack[-1][0] < num:
        _, index = stack.pop()
        answer[index] = num
        
    stack.append((num, i))
    

print(*answer)
