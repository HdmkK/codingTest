class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mem = []

        for i in range(len(nums)):

            if i == 0:
                mem.append(nums[0])
                continue

            mem.append(nums[i] + (mem[i-1] if mem[i-1] > 0 else 0))            

        return max(mem)

            
