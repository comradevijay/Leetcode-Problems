class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        smax = -1
        fmax = -1
        for i in range(len(nums)):
            if fmax < nums[i]:
                smax = fmax
                fmax = nums[i]
            elif smax < nums[i]:
                smax = nums[i]
        
        ans = (fmax - 1) * (smax - 1)
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna