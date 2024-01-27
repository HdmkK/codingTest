class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #오른쪽으로 누적곱한 배열
        #왼쪽으로 누적곱한 배열
        #이 두 배열을 조합하면 자기자신을 제외한 곱의 배열을 구할 수 있다.
        p = [1 for _ in range(len(nums))]
        q = [1 for _ in range(len(nums))]
        answer = [1 for _ in range(len(nums))]

        for i in range(1,len(nums)):
            p[i] *= p[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            q[i] *= q[i+1]*nums[i+1]

        for i in range(1, len(nums)-1):
            answer[i] *= p[i]*q[i]

        answer[0] *= q[0]
        answer[-1] *= p[-1]

        return answer


        





