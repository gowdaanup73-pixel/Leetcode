class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        return [k for k,v in count.items() if v > len(nums)//3]