from collections import deque

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    price = deque(map(int, input().split()))
    answer = []
    
    while price:
        
        cur_price = price.popleft()
        answer.append(str(cur_price))
        
        for i in range(len(price)):
            if int(price[i]/4)*3 == cur_price:
                del price[i]
                break
            
    answer = ' '.join(answer)
    print(f"#{test_case} {answer}")


