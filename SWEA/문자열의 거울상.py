string = list(input())


mem = {
    'b' : 'd',
    'd' : 'b',
    'p' : 'q',
    'q' : 'p'
}

answer = ""

for _ in range(len(string)):
    c = string.pop()
    answer += mem[c]
    
print(answer)
    

