class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total = last_a = last_b = last_c = 0    
        for at, ch in enumerate(s, 1):
            if ch == 'a':
                total += last_b if last_b <= last_c else last_c
                last_a = at
            elif ch == 'b':
                total += last_a if last_a <= last_c else last_c
                last_b = at
            else:
                total += last_a if last_a <= last_b else last_b
                last_c = at
        return total

        # n = len(s)
        # cnt = {'a': 0, 'b': 0, 'c': 0}
        # have = 0          
        # left = 0
        # ans = 0
        # for right in range(n):
        #     char = s[right]
        #     cnt[char] += 1
        #     if cnt[char] == 1:          
        #         have += 1
        #     while have == 3:
        #         ans += n - right
        #         left_char = s[left]
        #         cnt[left_char] -= 1
        #         if cnt[left_char] == 0:  
        #             have -= 1
        #         left += 1
        # return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna