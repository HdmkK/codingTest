class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        length = 0
        answer = []

        def dfs(cur, start):

            if len(cur) == length:
                answer.append(cur[:])
                return

            for idx, num in enumerate(nums[start:]):
                cur.append(num)
                dfs(cur, start + idx + 1)
                cur.pop()


        for k in range(len(nums)+1):
            length = k
            dfs([],0)

        return answer

