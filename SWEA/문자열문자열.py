N = int(input())
string = list(input())

answer = "No"

if len(string)%2 == 0:
    m = len(string)//2
    
    for i in range(m):
        if string[i] != string[i + m]:
            break
        
        if i == m-1:
            answer = "Yes"
        
print(answer)