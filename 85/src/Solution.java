import java.util.LinkedList;

/**
 * Created by Administrator on 2017/3/6.
 */
public class Solution {
    public static void main(String [] args){
        Solution s = new Solution();
        String [] temp = new String[]{"00000",
                                      "00000",
                                      "00000",
                                      "00000"};
        char[][] test = new char[temp.length][temp[0].length()];
        for(int i = 0; i < temp.length; i ++){
            for (int j = 0; j < test[0].length; j++){
                test[i][j] = temp[i].charAt(j);
            }
        }
        System.out.println(s.maximalRectangle(test));
    }
    class Node{
        public int a,b;
        Node(int a, int b){
            this.a = a;
            this.b = b;
        }
        Node cross(Node ano){
//            if (this.b <= ano.a || ano.b <= this.a)
//                return new Node(0,0);
            return new Node(Math.max(this.a, ano.a), Math.min(this.b, ano.b));
        }
    }
    private void findMax(LinkedList<Node>[] linkedArray, int row, Node begin, Node maxans, int n_layer){
        int length = begin.b - begin.a;
        if (length <= 0) return;
        if ((linkedArray.length - row + n_layer) * length < maxans.a)return;
        n_layer += 1;
        int ans_now = n_layer * length;
        if (ans_now > maxans.a)maxans.a = ans_now;
        if (row + 1 >= linkedArray.length) return;
        for (Node node: linkedArray[row+1]){
            findMax(linkedArray, row+1, node.cross(begin), maxans, n_layer);
        }
    }
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length, n = matrix[0].length;
        LinkedList<Node>[] linkedArray = new LinkedList[m];
        for(int i = 0; i < m; i++){
            linkedArray[i] = new LinkedList<Node>();
            int counter = 0;
            int j = 0;
            for(; j < n; j++){
                if (matrix[i][j] == '1') counter ++;
                else if (counter > 0){
                    linkedArray[i].add(new Node(j - counter, j));
                    counter = 0;
                }
            }
            if (counter > 0){
                linkedArray[i].add(new Node(j - counter, j));
            }
        }
        Node max_ans = new Node(0, 0);
        for(int i = 0; i < m; i++){
            for(Node k: linkedArray[i]){
                findMax(linkedArray, i, k, max_ans, 0);
            }
        }
        return max_ans.a;
    }
}
