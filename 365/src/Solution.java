
/**
 * Created by Administrator on 2017/3/6.
 */
public class Solution {
    public static void print(Object... args){
        for (Object o : args)
            System.out.print(o.toString() + ' ');
        System.out.println();
    }
    public static void main(String [] args){
        Solution s = new Solution();
        print(s.canMeasureWater(3, 5, 4), 3);
        print(s.canMeasureWater(0, 0, 0), 3);
        print(s.canMeasureWater(0, 0, 2), 3);
        print(s.canMeasureWater(3, 3, 6), 3);

    }
    public int GCD(int a, int b){
        while(b != 0){
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    public boolean canMeasureWater(int x, int y, int z) {
        if (z > x + y ) return false;
        if (z == 0 ) return true;
        return z % GCD(x, y) == 0;
    }
}
