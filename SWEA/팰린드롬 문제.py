from collections import deque

N, M = map(int, input().split())

    
def check(s):
    
    queue = deque(s)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
        
    return True


total_length = 0
not_palindrome = {}

for _ in range(N):
    s = input()
    if check(s):
        total_length = max(total_length, len(s))
    else:
        not_palindrome[s] = -1
        

for s, flag in not_palindrome.items():
    
    if flag == 1:
        continue
    
    stack = []
    for c in s:
        stack.append(c)
    
    reversed = ""
    while stack:
        reversed += stack.pop()
        
    if reversed in not_palindrome:
        total_length += len(s)*2
        not_palindrome[reversed] = 1
        
print(total_length)
        
        
        





    


