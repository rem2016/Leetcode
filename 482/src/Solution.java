/**
 * Created by Administrator on 2017/3/7.
 */
public class Solution {
    public static void main(String [] args){
        Solution s = new Solution();
        System.out.println(s.licenseKeyFormatting("1231b3213", 100));
        System.out.println(s.licenseKeyFormatting("1231a3213", 3));
        System.out.println(s.licenseKeyFormatting("1edA-a31231231-2-13", 3));
        System.out.println(s.licenseKeyFormatting("1edA-a31231231-2-13", 0));
        System.out.println(s.licenseKeyFormatting("", 8));
    }
    public String licenseKeyFormatting(String S, int K) {
        S = S.replaceAll("-", "");
        if (S.length() == 0)return S;
        StringBuilder sb = new StringBuilder();
        int first_num = 0;
        if (K == 0) first_num = S.length();
        else first_num = S.length() % K;
        // should I -1 ?
        if(first_num == 0) first_num = K;
        for(int j = 0; j < first_num; j++){
            char c = S.charAt(j);
            if (c <='z' && c>='a')
                c = Character.toUpperCase(c);
            sb.append(c);
        }
        if (first_num == S.length())
            return sb.toString();
        for(int i = first_num; i < S.length(); i+=K){
            sb.append('-');
            for(int j = 0; j < K; j++){
                char c = S.charAt(i + j);
                if (c <='z' && c>='a')
                    c = Character.toUpperCase(c);
                sb.append(c);
            }
        }
        return sb.toString();
    }
}
