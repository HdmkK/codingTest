import collections
N = int(input())

words = []
for _ in range(N):
    words.append(input())
    
count = 0
    
def dfs(cur, start, k):
    
    if len(cur) == k:
        #알파벳이 모두 들어있는지 확인
        string = ''.join(cur)
        mem = collections.Counter(string)
        for c in range(ord('a'), ord('z')+1):
            if chr(c) not in mem:
                return
        global count
        count += 1
        return
    
    for i in range(start, N):
        cur.append(words[i])
        dfs(cur, i+1, k)
        cur.pop()
    
    
for k in range(1, N+1):
    dfs([], 0, k)
    
print(count)