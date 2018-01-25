class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        list<int>* candidates = new list<int>();
        candidates->push_back(0);
        if (s3.size() != s1.size() + s2.size()){
            return false;
        }
        for (int i = 0; i < s3.size(); i++){
            list<int>* new_candidates = new list<int>();
            int last_v = -1;
            for (auto iter = candidates->begin(); iter != candidates->end(); iter++){
                if (i - *iter < s2.size() && s3[i] == s2[i - *iter]) {
                    if (*iter != last_v) new_candidates->push_back(*iter);
                }
                if (*iter < s1.size() && s3[i] == s1[*iter]) {
                    new_candidates->push_back(*iter + 1);
                    last_v = *iter + 1;
                }
            }
            if (new_candidates->empty()){
                return false;
            }
            candidates = new_candidates;
        }
        return true;
    }
};