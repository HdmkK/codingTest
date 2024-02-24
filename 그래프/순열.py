class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        def dfs(cur):

            # 숫자를 나열했으면 answer에 추가
            if len(cur) == len(nums):
                answer.append(cur[:])
                return

            #현재 단계에서 입력 가능한 num을 차례대로 고려
            for num in nums:
                if num not in cur: #이미 cur에 입력한 num이라면 무시
                    cur.append(num)
                    dfs(cur)
                    cur.pop()

        dfs([])
        return answer