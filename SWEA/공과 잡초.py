string = list(input())

cur = 0
count = 0
while cur < len(string):
    if string[cur] == '(':
        count += 1
        cur += 1
       
    elif string[cur] == ')':
        count += 1
        
    cur += 1
print(count)
    
    