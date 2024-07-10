from collections import deque

def solution(cards1, cards2, goal):
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    
    for target in goal:
        if queue1 and target == queue1[0]:
            queue1.popleft()
        elif queue2 and target == queue2[0]:
            queue2.popleft()
        else:
            return "No"
    return "Yes"
    
    
    