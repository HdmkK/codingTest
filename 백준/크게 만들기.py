length, K = map(int, input().split())
num = input()

stack = []

for c in num:
    
    while stack and stack[-1] < c and K > 0:
        stack.pop()
        K-=1
    stack.append(c)

if K > 0:
    print("".join(stack[:-K]))
else:
    print("".join(stack))
    

