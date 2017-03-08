package com.company;

import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;

public class Solution {
    public static void print(Object... a){
        for (Object i: a)
            System.out.print(i.toString() + " ");
        System.out.println();
    }
    public static void main(String args[]){
        Solution s = new Solution();
        print(s.uniquePathsWithObstacles(
                new int[][]{
                        {0, 0, 0},
                        {0, 1, 0},
                        {0, 0, 0}}));
        print(s.uniquePathsWithObstacles(
                new int[][]{
                        {1, 1, 1},
                        {0, 0, 0},
                        {0, 0, 0}}));
    }

    static class Node {
        public int x, y;
        public Node(int xx, int yy){
            this.x = xx;
            this.y = yy;
        }
    }
    public int uniquePaths(int m, int n) {
        if (m * n == 0)
            return 0;
        int map[][] = new int[m+2][n+2];
        map[1][1] = 1;
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(1, 1));
        while(!q.isEmpty()){
            Node peek = q.poll();
            int x = peek.x, y = peek.y;
            if (x > m || y > n) continue;
            if (x != 1 && y!= 1 && map[x][y] != 0) continue;
            if (map[x][y] == 0) map[x][y] = map[x-1][y] + map[x][y-1];
            q.add(new Node(x+1, y)); q.add(new Node(x, y+1));
        }
        return map[m][n];
    }
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        if (m == 0) return 0;
        int n = obstacleGrid[0].length;
        if (n == 0) return 0;

        int map[][] = new int[m+2][n+2];
        boolean visited[][] = new boolean[m+2][n+2];
        map[1][1] = 1;
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(1, 1));
        while(!q.isEmpty()){
            Node peek = q.poll();
            int x = peek.x, y = peek.y;
            if (x > m || y > n) continue;
            if (obstacleGrid[x - 1][y - 1] == 1) {
                map[x][y] = 0;
                continue;
            }
            if (map[x][y] == 0) map[x][y] = map[x-1][y] + map[x][y-1];
            if (!visited[x+1][y]){
                q.add(new Node(x+1, y));
                visited[x+1][y] = true;
            }
            if (!visited[x][y+1]){
                q.add(new Node(x, y+1));
                visited[x][y+1] = true;
            }
        }
        return map[m][n];


    }
}
