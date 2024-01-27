class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        #배열에서 제일 작은 수를 처리하기 위해선 어짜피 다른 수가 희생되어야 한다.
        #따라서 이왕이면 그나마 작은 수를 희생
        #ex) min(1, 6)보다는 min(1, 2)로 두면 6은 다른 곳에서 활용가능
        #따라서 오름차순으로 정렬하고 두개씩 pair를 묶는 것이 정답
        nums.sort()

        sum = 0
        for i in range(0, len(nums), 2):
            sum += min(nums[i], nums[i+1])

        return sum
