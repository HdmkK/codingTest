class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
            
        a = self.majorityElement(nums[:len(nums)//2])
        b = self.majorityElement(nums[len(nums)//2:])

        return [b, a][nums.count(a) > len(nums)//2]