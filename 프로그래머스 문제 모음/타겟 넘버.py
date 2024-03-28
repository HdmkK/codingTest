def solution(numbers, target):
    
    def dfs(cur, i):
        
        global answer
        
        if i == len(numbers):
            if sum(cur) == target:
                return 1
            else:
                return 0
        
        cur.append(numbers[i])
        a = dfs(cur, i+1)
        cur.pop()
        cur.append(-numbers[i])
        b = dfs(cur, i+1)
        cur.pop()
        
        return a+b
    
    return dfs(cur=[],i=0)
    
    