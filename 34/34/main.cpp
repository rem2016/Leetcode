#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <stack>
#include <map>

typedef long long ll;
#define TEST 1
using namespace std;


class Solution {
public:
	vector<int> searchRange(vector<int>& nums, int target) {
		int n = nums.size();
		int l = 0, r = n, lans = -1, rans = -1, m=0;
		vector<int > ans = {-1, -1};
		if (n == 0)return ans;

		while (l < r) {
			m = (l + r) / 2;
			if (nums[m] >= target) {
				r = m;
			}
			else l = m + 1;
		}
		if (l >= n || nums[l] != target) {
			return ans;
		}
		lans = l;
		l = 0, r = n;
		while (l < r) {
			m = (l + r) / 2;
			if (nums[m] <= target) {
				l = m + 1;
			}
			else r = m;
		}
		rans = l - 1;
		ans[0] = lans;
		ans[1] = rans;
		return ans;
	}
};


int main() {
	
	Solution s;
	vector<int > a = {1,2,2,2,2,2,2,3,4,5};
	auto ans = s.searchRange(a, 2);
	cout << ans[0] <<ans[1] << endl;

	vector<int > b = {};
	ans = s.searchRange(b, 3);
	cout << ans[0] <<ans[1] << endl;

	vector<int > c = {3};
	ans = s.searchRange(c, 3);
	cout << ans[0] <<ans[1] << endl;

	vector<int > d = {2, 1};
	ans = s.searchRange(d, 3);
	cout << ans[0] <<ans[1] << endl;

	getchar();
}