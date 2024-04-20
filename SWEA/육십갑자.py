TC = int(input())


    
    
for tase_case in range(1, TC+1):
    
    N, M = map(int, input().split())
    s = input().split()
    t = input().split()

    Q = int(input())
    q = []
    for _ in range(Q):
        q.append(int(input()))
    
    answer = f"#{tase_case}"
    
    for year in q:
        year-=1
        answer = answer + " " + s[year%N] + t[year%M]
    print(answer)
    