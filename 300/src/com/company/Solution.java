package com.company;

import java.util.Objects;

public class Solution {
    public static void print(Object... args){
        for (Object a: args){
            System.out.print(a.toString() + ' ');
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        print(s.lengthOfLIS(new int[]{10,9,2,5,3,7,101,18})); // 4
        print(s.lengthOfLIS(new int[]{1, 100, 2, 200, 3})); // 3
        print(s.lengthOfLIS(new int[]{4, 3, 2, 0, 1, 2, 3})); // 4
        print(s.lengthOfLIS(new int[]{0, 1, 2, 3})); // 4
        print(s.lengthOfLIS(new int[]{1, 2, 3, 2, 1, 1, 1, 2, 5,}));// 3
    }
    public int lengthOfLIS(int[] nums) {
        int [] max = new int [nums.length];
        if (nums.length == 0) return 0;
        max[0] = 1;
        int max_ans = 1;
        for (int i = 1; i < nums.length; i++){
            max[i] = 1;
            for (int j = 0 ; j < i; j++){
                if (nums[i] <= nums[j]){
                    continue;
                }
                int temp = max[j] + 1;
                if(temp > max[i]){ max[i] = temp; }
            }
            if (max[i] > max_ans) max_ans = max[i];
        }
        return max_ans;
    }
}
