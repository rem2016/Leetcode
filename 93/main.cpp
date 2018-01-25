class Solution {
private:
    bool isValid(string s){
        if (s.size() == 0 || (s[0] == '0' && s.size() != 1))
            return false;
        if (s.size() < 3)
            return true;
        
        if (s[0] < '2')
            return true;
        if (s[0] > '2')
            return false;
        
        if (s[1] < '5')
            return true;
        if (s[1] > '5')
            return false;
        
        if (s[2] > '5')
            return false;
        return true;
    }
    void _restoreIp(string s, int leftField, string tempAns, vector<string>& ans){
        if (leftField == 1 && isValid(s) ){
            ans.push_back(tempAns + '.' + s);
            return;
        }
        if (s.size() > leftField * 3){
            return;
        }
        int maxLength = min(3, int(s.size() - leftField + 1));
        if (s[0] == '0'){
            maxLength = 1;
        }
        for (int length = max(1, int(s.size() - (leftField - 1)*3)); length <= maxLength; length++){
            if (length < 3 || isValid(s)){
                string sub = s.substr(0, length);
                _restoreIp(s.substr(length), leftField-1, tempAns.size()==0?sub:tempAns+"."+sub, ans);
            }
        }
    }
    
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> ans;
        _restoreIp(s, 4, "", ans);
        return ans;
    }
};