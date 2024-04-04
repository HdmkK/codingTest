def solution(s):
    answer = True
    
    stack = []
    
    for c in s:
        if stack and c == ')' and stack[-1]:
            stack.pop()
        else:
            stack.append(c)
            
    return True if not stack else False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True