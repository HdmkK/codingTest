from collections import deque

T = int(input())

i = 0
for _ in range(T):
    
    string = input()
    
    s = deque(string)
    
    answer = "YES"
    left = 0
    right = len(s)
    
    while len(s) > 1:
        
        a = s.popleft()
        b = s.pop()
        
        if a != b:
            answer = "NO"
            break
        

    s = deque(string[:int((len(string)-1)/2)])
        
    while len(s) > 1:
        
        a = s.popleft()
        b = s.pop()
        
        if a != b:
            answer = "NO"
            break
        
    s = deque(string[-int((len(string)-1)/2):])
        
    while len(s) > 1:
        
        a = s.popleft()
        b = s.pop()
        
        if a != b:
            answer = False
            break
        
    i+=1
    print(f"#{i} {answer}")
        