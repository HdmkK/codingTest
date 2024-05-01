def solution(begin, target, words):
    answer = 0
    
    min_v = len(words) + 1
    
    def dfs(cur_word, visited, k):
        
        if k >= 0:
            if cur_word == target:
                nonlocal min_v
                min_v = min(min_v, len(words)-k)
                return
        else:
            return
            
                
            
        
        
        for i in range(len(cur_word)):
            test = cur_word[:i] + cur_word[i+1:]
            for j in range(len(words)):
                if not visited[j] and (words[j][:i] + words[j][i+1:]) == test:
                    visited[j] = True
                    dfs(words[j], visited[:], k-1)
                    visited[j] = False
                
    
    
    visited = [False for _ in range(len(words))]
    dfs(begin, visited, len(words))
    
    if min_v == len(words) + 1:
        return 0
    else:
        return min_v