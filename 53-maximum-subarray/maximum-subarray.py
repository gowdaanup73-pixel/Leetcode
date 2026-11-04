class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = nums[0]
        maximum = nums[0]
        for num in nums[1:]:
            maximum = max(num,maximum+num)
            sum = max(sum,maximum)
        return sum