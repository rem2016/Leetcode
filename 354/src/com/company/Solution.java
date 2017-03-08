package com.company;

import java.lang.reflect.Array;
import java.util.*;

public class Solution {

    public static void print(Object... args){
        for (Object a: args){
            System.out.print(a.toString() + ' ');
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        print(s.maxEnvelopes(new int [][]{})); // 0
        print(s.maxEnvelopes(new int [][]{{1,1}})); // 1
        print(s.maxEnvelopes(new int [][]{{1,2}, {3, 4}, {8,0}, {1, 1}})); // 2
        print(s.maxEnvelopes(new int [][]{{1,2}, {3, 4}, {8,4}, {1, 1}})); // 2
        print(s.maxEnvelopes(new int [][]{{10,5}, {1, 1}, {6,6}, {5, 5}})); // 3
        print(s.maxEnvelopes(new int [][]{{20,6}, {1, 1}, {6,6}, {5, 5}, {7, 4}, {8, 5}})); // 4
        print(s.maxEnvelopes(new int [][]{{100,100}, {1,2}, {3, 4}, {8,5}, {1, 1}})); // 4
    }

    public int maxEnvelopes(int[][] envelopes) {
        if (envelopes.length == 0)return 0;
        Arrays.sort(envelopes, (a, b) -> a[0] == b[0]? b[1] - a[1] : a[0] - b[0]);
        int [] ans = new int[envelopes.length];
        int len = 0;
        for (int[] env: envelopes){
            int index = Arrays.binarySearch(ans, 0, len, env[1]);
            if(index < 0)index = - (index + 1);
            ans[index] = env[1];
            if (index == len) ++len;
        }
        return len;
    }
}
