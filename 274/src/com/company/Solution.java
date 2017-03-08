package com.company;

public class Solution {

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.hIndex(new int[]{3, 0, 1, 6, 5}));
        System.out.println(s.hIndex(new int[]{0}));
        System.out.println(s.hIndex(new int[]{}));
        System.out.println(s.hIndex(new int[]{1}));
        System.out.println(s.hIndex(new int[]{2, 2}));
        System.out.println(s.hIndex(new int[]{2, 1}));

    }

    public int hIndex(int[] citations) {
        int n = citations.length;
        int [] record = new int[n + 1];
        for (int c: citations){
            if (c >= n){
                record[n] += 1;
                continue;
            }
            record[c] += 1;
        }
        int i = n;
        for (; i > 0; i--){
            record[i - 1] += record[i];
            if (record[i] >= i){
                break;
            }
        }
        return i;
    }
}
