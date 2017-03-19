#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<stack>

using namespace std;
typedef long long ll;

class Solution {
public:
	int search(vector<int>& nums, int target) {
		stack<pair<int, int> > p;
		p.push(make_pair(0, nums.size()));
		while (!p.empty()) {
			pair<int, int> np = p.top();
			int l = np.first, r = np.second;
			p.pop();
			if (l == r)continue;
			if (nums[l] < nums[r-1]) {
				int m;
				while (l != r) {
					m = (r + l)/2;
					if (nums[m] == target)return m;
					else if (nums[m] < target) l = m + 1;
					else r = m;
				}
			}
			int m = (np.first + np.second) / 2;
			if (nums[m] == target)return m;
			if (nums[m] > target) {
				if (nums[m] > nums[np.second - 1] && target <= nums[np.second - 1]) {
					p.push(make_pair(m + 1, np.second));
				}
				p.push(make_pair(np.first, m));
			}
			else {
				if (nums[m] < nums[np.first] && target >= nums[np.first]) {
					p.push(make_pair(np.first, m));
				}
				p.push(make_pair(m + 1, np.second));
			}
		}
		return -1;
	}
};

int main() {
	Solution s;
	int _a[] = {1,2,3,4,5,-1,-2,-3};

	vector<int> b = {1,2,3, -2, -1, 0};
	cout << s.search(b, 1) << endl;
	getchar();
}