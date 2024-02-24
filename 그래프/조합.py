class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        answer = []

        def dfs(cur, start):

            if len(cur) == k:
                answer.append(cur[:])
                return
            
            #후보 숫자인 1~n 중에서 num(num<start)을 뽑는 경우는 이미 이전 단계에서 고려했을 것이므로 제외
            for num in range(start, n+1):
                cur.append(num)
                dfs(cur, num+1)
                cur.pop()
        
        dfs([],1)
        
        return answer
        