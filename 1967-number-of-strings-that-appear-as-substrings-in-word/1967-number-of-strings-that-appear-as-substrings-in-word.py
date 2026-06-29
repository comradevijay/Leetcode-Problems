class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for i in patterns:
            if i in word:
                ans += 1
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna