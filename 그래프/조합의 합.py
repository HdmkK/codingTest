class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []

        def dfs(cur, start):

            if sum(cur) == target:
                answer.append(cur[:])
                return

            #자신을 포함해서 뽑기 후보에 고려(단, 조합이므로 start 이전 num은 고려X)
            for idx, num in enumerate(candidates[start:]):
                if sum(cur) + num <= target:
                    cur.append(num)
                    dfs(cur, start + idx)
                    cur.pop()

        dfs([], 0)

        return answer