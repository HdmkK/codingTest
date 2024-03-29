from collections import defaultdict

def solution(n, computers):
    answer = 0
    
    graph = {}
    
    
    #graph로 변환
    for i, i_list in enumerate(computers):
        graph[i] = []      
        for j, j_value in enumerate(i_list):        
            if j_value == 1:
                if i != j:
                    graph[i].append(j)
            
    network_count = 0
    visited = {}
    #탐색
    
    def dfs(n):
        
        for item in graph[n]:
            if item not in visited:
                visited[item] = -1
                dfs(item)
    
    
    for start_node in graph.keys():
        
        if start_node not in visited:
            visited[start_node] = -1
            dfs(start_node)
            network_count+=1
               
    return network_count