/**
 * Created by Administrator on 2017/3/6.
 */
public class Solution {
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.println(s.rob(new int[]{1,2,1,2,1})); // 4
        System.out.println(s.rob(new int[]{9,2,1,2,1})); // 11
        System.out.println(s.rob(new int[]{9,20,1,2,1})); // 22
    }
    public int rob(int[] nums) {
        if (nums.length == 0)return 0;
        if (nums.length == 1) return nums[0];
        int ans[] = new int[nums.length];
        ans[0] = nums[0];
        for(int i = 1; i < nums.length; i++){
            ans[i] = nums[i];
            for(int j = Math.max(0, i - 3); j < i - 1; j ++){
                if(nums[i] + ans[j] > ans[i])
                    ans[i] = nums[i] + ans[j];
            }
        }
        return Math.max(ans[ans.length - 1], ans[ans.length - 2]);
    }
}
