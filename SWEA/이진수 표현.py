import collections

N, M = map(int, input().split())

queue = collections.deque()


if M == 0:
    print("OFF")
else:
    n = M
    while n > 1:
        
        share = n // 2
        remainder = n % 2
        
        queue.appendleft(remainder)
        n = share
        
    queue.appendleft(1)
    ret = list(queue)

    if ret[-N:] == [1 for _ in range(N)]:
        print("ON")
    else:
        print("OFF")
        


