/**
 * Created by Administrator on 2017/3/3.
 */

public class Solution {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hIndex(new int[]{10, 11, 13, 15, 16})); // 5
        System.out.println(s.hIndex(new int[]{0, 4, 4, 5, 6})); // 4
        System.out.println(s.hIndex(new int[]{0})); // 0
        System.out.println(s.hIndex(new int[]{0, 1, 3, 5, 6})); // 3
        System.out.println(s.hIndex(new int[]{}));
        System.out.println(s.hIndex(new int[]{1})); // 1
        System.out.println(s.hIndex(new int[]{2, 2})); // 2
        System.out.println(s.hIndex(new int[]{1, 2})); // 1
        System.out.println(s.hIndex(new int[]{1, 1})); // 1
        System.out.println(s.hIndex(new int[]{0,0,0, 0, 1})); // 1


    }

    public int hIndex(int[] citations) {
        if (citations.length == 0)return 0;
        if (citations[citations.length - 1] == 0) return 0;
        int l = 0, r=citations.length -1, n = citations.length;
        while (l != r){
            int m = (l + r) / 2;
            if (n - m < citations[m]){
                r = m;
            }else{
                l = m;
            }
            if (l + 1 == r){
                if (n - l <= citations[l])r = l;
                else l = r;
            }
        }
        return n - l;
    }
}
