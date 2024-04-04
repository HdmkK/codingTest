from collections import deque

#다음 탐색후보단어를 알아내는 함수
def get_next_search_word(current_word, words):
    
    for word in words:
        
        #현재 단어랑 단어 하나만 차이날 경우, 탐색후보에 추가
        count = 0
        for w, c in zip(word, current_word):
            
            if w != c:
                count+=1
                
        if count == 1:
            yield word
                
    

def solution(begin, target, words):
    answer = 0
    
    #방문여부와 거리를 저장할 dict
    mem = {
        begin: 0
    }
    
    #BFS용 큐
    queue = deque([begin])
    
    while queue:
        current_word = queue.popleft()
        
        if current_word == target:
            break
        
        #탐색후보들을 찾아내서
        next_word_list = get_next_search_word(current_word, words)
        
        #방문하지 않았다면 방문예약(길이도 dict에 갱신)
        for next_word in next_word_list:
            if next_word not in mem:
                mem[next_word] = mem[current_word] + 1
                queue.append(next_word)
                
    return mem.get(target, 0)
        
    