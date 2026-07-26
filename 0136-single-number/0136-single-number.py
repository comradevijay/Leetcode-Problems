class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # for i in range(len(nums)):
        #     if nums.count(nums[i]) == 1:
        #         return nums[i]

        m = 0
        for i in nums:
            m = m^i
        return m
        