T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, D = map(int, input().split())

    cur = 1
    mark = 0
    count = 0

    if N < 2*D + 1:
        count = 1
    else:
        cur += D
        while cur + D <= N:
            count+=1
            mark = cur + D
            cur += 2*D + 1
            
        
        if mark < N:
            count+=1
            
    print("#{} {}".format(test_case, count))
    