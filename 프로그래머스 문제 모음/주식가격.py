def solution(prices):
    answer = []
    
    for i in range(len(prices)-1, -1, -1):
        answer.append(i)
        
    stack = []
    
    for idx, p in enumerate(prices):
        
        while stack and stack[-1][0] > p:
            answer[stack[-1][1]] = idx-stack[-1][1]
            stack.pop()
            
        stack.append((p,idx))
        
    return answer