#include<vector>
#include<string>
#include<stdio.h>
#include<iostream>
#include<stack>
#include<queue>

using namespace std;


class Solution {
public:
	void dfs(vector<string> &ans, string now, int left_num, int n) {
		if (n == now.size()) {
			ans.push_back(string(now));
			return;
		}
		int right_num = now.size() - left_num, unmatch_num = left_num - right_num;
		if (unmatch_num > 0) {
			dfs(ans, now + ')', left_num, n);
		}
		if (left_num < n / 2) {
			dfs(ans, now + '(', left_num + 1, n);
		}
		return;
	}
	vector<string> generateParenthesis(int n) {
		n *= 2;
		vector<string> ans;
		dfs(ans, "(", 1, n);
		return ans;
	}
};

int main() {
	Solution s;
	auto ans = s.generateParenthesis(14);
	for_each(ans.begin(), ans.end(), [&](string s){
		cout << s << endl;
	});
	getchar();
	return 0;
}