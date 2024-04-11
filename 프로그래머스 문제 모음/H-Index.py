def solution(citations):
    
    
    
    max_h = 0
    h = 1
    
    while True:
        
        if h > len(citations):
            break
        
        count = 0
        for idx, c in enumerate(citations):
            if c >= h:
                count += 1
                
        if count >= h:
            max_h = max(max_h, h)
            
        h+=1
                  
    return max_h