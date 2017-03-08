import java.util.Arrays;
import java.util.List;

/**
 * Created by Administrator on 2017/3/2.
 */
public class Solution {
    public static void main(String args[]){
        Solution s = new Solution();
        System.out.println(s.maxProduct(new int[]{3, -1, 4}));// 4
        System.out.println(s.maxProduct(new int[]{-2, -5})); // 10
        System.out.println(s.maxProduct(new int[]{3, -1, 4, -1}));// 12
        System.out.println(s.maxProduct(new int[]{-2, -3, 7})); // 42
        System.out.println(s.maxProduct(new int[]{-2, -3, 7, -4, -5})); // 840
        System.out.println(s.maxProduct(new int[]{-2, -3, 7, -4, 0, -5})); // 840
        System.out.println(s.maxProduct(new int[]{0}));
        System.out.println(s.maxProduct(new int[]{6}));
    }
    public int maxProduct(int[] nums) {
//        System.out.println("===============");
        int [] maxPositive = new int[nums.length];
        int [] maxN = new int[nums.length];
        int [][] maxs = new int[][]{maxN, maxPositive};
        int maxAns = nums[0];
        boolean hasZero=false;
        if (nums[0] > 0){maxPositive[0] = nums[0];}
        else if (nums[0] < 0){maxN[0] = -nums[0]; }
        else hasZero = true;
        for(int i = 1; i < nums.length; i++){
            int isPositive = 1, num = nums[i], absnum = Math.abs(num);
            if (num == 0){
                hasZero = true;
                continue;
            }
            if (nums[i] < 0) isPositive = 0;
            maxs[isPositive][i] = Math.max(absnum * maxs[1][i - 1], absnum);
            maxs[1 - isPositive][i] = absnum * maxs[0][i - 1];
            if ( maxs[1][i] > maxAns){
                maxAns = maxs[1][i];
            }else if( -maxs[0][i] > maxAns){
                maxAns = - maxs[0][i];
            }
        }
//        for(int [] list: maxs){
//            for(int i: list){
//                System.out.print(i);
//                System.out.print('\t');
//            }
//            System.out.println();
//        }
        if (hasZero && maxAns < 0){
            return 0;
        }
        return maxAns;
    }
}
