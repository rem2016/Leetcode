import javax.swing.tree.TreeNode;
import java.util.*;
import java.util.stream.Collectors;

/**
 * Created by Administrator on 2017/3/7.
 */
class TreapNode{
    TreapNode l, r, father;
    int val, ln, rn;
    TreapNode(int val, TreapNode father){
        l = r = null;
        this.val = val;
        this.father = father;
        this.ln = 0;
        this.rn = 0;
    }
    void insert(int val){
        if (val > this.val){
            this.rn += 1;
            if(this.r == null){
                this.r = new TreapNode(val, this);
                return;
            }
            this.r.insert(val);
        }else{
            this.ln += 1;
            if(this.l == null){
                this.l = new TreapNode(val, this);
                return;
            }
            this.l.insert(val);
        }
    }
    int count(int val){
        if(this.val > val)return this.l != null ? this.l.count(val):0;
        if(this.val < val)return 1 + this.ln + (this.r != null? this.r.count(val):0);
        return this.ln;
    }
    TreapNode search(int val){
        if(this.val > val)return this.l.search(val);
        if(this.val < val)return this.r.search(val);
        return this;
    }
    void remove(){
        if(this.father == null) return ;
        if(this == this.father.l) {
            this.father.l = this.l != null ? this.l : this.r;
        }
        if(this == this.father.r){
            this.father.r = this.l != null ? this.l : this.r;
        }
        TreapNode son = this;
        while(father != null){
            if (son == father.l)father.ln -= 1;
            if (son == father.r)father.rn -= 1;
            son = father;
            father = father.father;
        }
    }


}
public class Solution {
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.println(s.countSmaller(new int[]{1,2,3}));
        System.out.println(s.countSmaller(new int[]{1,2,3,2,4,5,2}));
        System.out.println(s.countSmaller(new int[]{3,2,1}));
    }
    public List<Integer> countSmaller(int[] nums) {
        if (nums.length == 0) return Arrays.asList();
        if (nums.length == 1) return Arrays.asList(0);
        List<Integer> list_nums = Arrays.stream(nums).boxed().collect(Collectors.toList());
        TreapNode root = new TreapNode(-2147483648, null);
        List<Integer> ans_list = new ArrayList<>(nums.length);
        for(int i = 0; i < nums.length; i++){
            root.insert(list_nums.get(i));
        }
        for(int i = 0; i < nums.length; i++){
            int val = list_nums.get(i);
            Integer ans = root.count(val);
            ans_list.add(ans);
            root.search(val).remove();
        }
        return ans_list;
    }
}
