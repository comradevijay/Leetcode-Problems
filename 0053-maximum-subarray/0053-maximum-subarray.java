class Solution {
    public int maxSubArray(int[] nums) {
        int ans = nums[0];
        int summ = 0;

        for (int num : nums) {
            summ = Math.max(num, summ + num);
            ans = Math.max(ans, summ);
        }
        
        return ans;
    }
}







