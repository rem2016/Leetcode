/**
 * Created by Administrator on 2017/3/6.
 */
public class Solution {
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.println(s.rob(new int[]{1,2,3})); // 4
        System.out.println(s.rob(new int[]{4,1,2,3})); // 4
        System.out.println(s.rob(new int[]{5,1,2,3})); // 4
    }
    public int rob(int [] nums){
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[1];
        return Math.max(rob1(nums, 0, nums.length - 2), rob1(nums, 1, nums.length - 1));
    }
    public int rob1(int[] nums, int l, int r) {
        int include=0, exclude=0;
        int e = 0, in = 0;
        for(int i = l; i <= r; i++){
            include = nums[i] + e;
            exclude = Math.max(in, e);
            in = include; e = exclude;
        }
        return Math.max(include, exclude);
    }
}
