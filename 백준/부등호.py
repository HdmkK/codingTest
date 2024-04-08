K = int(input())

symbols = input().split()

mem = {}
max_value = 0
min_value = 9876543210

#순열을 만들어가자(부등호를 만족하는지 확인해가면서)

def check(a, b, ops):
    if ops == '>':
        return a > b
    elif ops == '<':
        return a < b

def backtracking(curr, idx):
    
    if idx == K+1:
        global max_value
        global min_value
        a = int("".join(map(str, curr)))
        max_value = max(max_value, a)
        min_value = min(min_value, a)
        return
    
    for num in range(10):
        if num not in mem:
            
            curr.append(num)
            mem[num] = -1
            
            if idx >= 1 and not check(curr[idx-1], curr[idx], symbols[idx-1]):
                curr.pop()
                del mem[num]
                continue
            
            backtracking(curr, idx+1)
            curr.pop()
            del mem[num]

backtracking([], 0)

max_value = str(max_value)
min_value = str(min_value)

while len(max_value) < K+1:
    max_value = '0' + max_value
while len(min_value) < K+1:
    min_value = '0' + min_value
    
print(max_value)
print(min_value)
   