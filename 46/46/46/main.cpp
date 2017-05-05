#include <stdio.h>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>

typedef long long ll;
using namespace std;

class Solution {
private:
	void _permute(deque<int>& left_nums, vector<vector<int> >& ans, vector<int>& this_nums) {
		if (left_nums.size() == 0) {
			ans.push_back(this_nums);
			return;
		}
		for (int i = 0; i < left_nums.size(); i++) {
			int backup = *left_nums.rbegin();
			left_nums.pop_back();
			this_nums.push_back(backup);
			_permute(left_nums, ans, this_nums);
			left_nums.push_front(backup);
			this_nums.pop_back();
		}
		return;
	}
	
public:
	vector<vector<int> > permute(vector<int>& nums) {
		sort(nums.begin(), nums.end());
		vector<vector<int> > ans;
		vector<int> insert_nums;
		deque<int> dnums;
		for (vector<int>::iterator iter = nums.begin(); iter != nums.end(); iter++) {
			dnums.push_back(*iter);
		}
		_permute(dnums, ans, insert_nums);
		return ans;
	}
};

int main() {
	Solution s;
	vector<int> a;
	a.push_back(1);
	a.push_back(2);
	a.push_back(3);
	a.push_back(4);
	auto ans = s.permute(a);
	for (int i = 0; i < ans.size(); i++) {
		for (int j = 0; j < ans[i].size(); j++) {
			cout << ans[i][j] << ' ';
		}
		cout << endl;
	}
	getchar();
}