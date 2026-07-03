class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> hm = new HashMap<>();
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            Integer key = nums[i];
            hm.put(key, hm.getOrDefault(key, 0)+1);
        }
        for (Integer num : hm.keySet()) {
            if (hm.get(num) > nums.length/2) {
                res =  num;
            }
        }
        return res;
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna