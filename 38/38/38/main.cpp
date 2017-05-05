#include<vector>
#include<string>
#include<list>
#include<iostream>
#include<stack>

typedef long long ll;
using namespace std;

class Solution {
public:
	string countAndSay(int n) {
		if (n == 1) { return "1"; }

		string a = countAndSay(n - 1);
		char last_word = 0;
		int count = 0;
		string ans;
		for (int i = 0; i < a.size(); i++) {
			if (last_word == 0) {
				last_word = a[i];
				count = 1;
				continue;
			}
			if (a[i] == last_word) {
				++count;
			}
			else {
				ans += to_string(count);
				ans += last_word;
				last_word = a[i];
				count = 1;
			}
		}
		ans += to_string(count);
		ans += last_word;
		cout << ans << endl;
		return ans;
	}
};

int main() {
	Solution s;
	s.countAndSay(10);
	getchar();
}