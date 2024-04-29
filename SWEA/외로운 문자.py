string = list(input())

cur = 0

while cur < len(string)-1:
    
    flag = False
    for i in range(cur+1, len(string)):
        if string[cur] == string[i]:
            string.pop(i)
            string.pop(cur)
            flag = True
            break
    if not flag:
        cur+=1
if not string :
    print("Good")
else:
    string.sort()
    print(''.join(string))