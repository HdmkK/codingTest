X, Y = map(int, input().split())


def Rev(num):
    
    num = str(num)

    stack = []

    for c in num:
        stack.append(c)
        
    rev_num = ""

    for _ in range(len(stack)):
        rev_num += stack.pop()
        
    return int(rev_num)

print(Rev(Rev(X)+Rev(Y)))



