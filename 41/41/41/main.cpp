#include <stdio.h>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <string>

typedef long long ll;
using namespace std;


class Solution {
public:
	int firstMissingPositive(vector<int>& nums) {
		if (nums.size() == 0 ) return 1;
		for (int i = 0; i < nums.size(); i++) {
			int num = nums[i];
			if (num > 0 && num <= nums.size()) {
				if (num == nums[num-1]) continue;
				swap(nums[i], nums[num-1]);
				--i;
			}
		}
		for (int i = 0; i < nums.size(); i++) {
			if (i + 1 != nums[i]) {
				return i + 1;
			}
		}
		return nums.size() + 1;
	}

};

int main() {

	int a[] = {1, 2, 3};
	vector<int> b(a, a + 0);
	Solution s;
	cout << s.firstMissingPositive(b) << endl;
	getchar();

}