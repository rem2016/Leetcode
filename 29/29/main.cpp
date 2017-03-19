#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <stack>
#include <valarray>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std;
typedef long long ll;

class Solution {
public:
	int divide(int raw_dividend, int raw_divisor) {
		#define MAXINT 2147483647ll
		// 必须在这里进行显式转换，隐式转换会将MININT转变为正数
		ll dividend = (ll)raw_dividend, divisor = (ll)raw_divisor;
		ll ans = 0;
		bool is_neg = ((dividend > 0) ^ (divisor > 0));
		dividend = abs(dividend); divisor = abs(divisor);
		for (int i = 31; i >= 0; i--) {
			ll newv = divisor << i;
			if (newv > dividend) continue;
			dividend -= newv;
			ans |= (1 << i);
		}
		if (is_neg) {
			if (ans < 0) return ans;
			return -ans;
		}
		if (ans<0 || ans > MAXINT) return MAXINT;
		return ans;
	}
};


int main() {
	Solution s;
	cout << s.divide(-2147483648, -1) << endl;
	cout << s.divide(-2147483648, 1) << endl;
	cout << s.divide(5, -1) << endl;
	getchar();
}