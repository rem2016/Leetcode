#include<stdio.h>
#include<string>
#include<stdlib.h>
using namespace std;

class Solution {
public:
    int myAtoi(string stri) {
		const int MAXINT = 2147483647;
		const int MININT = -2147483648;
		int ans = 0, last_num = 0;
		int isNe = 0, first = 0, flag=0;
		int overflow = 0;
		int i = 0;
		for (i = 0; i < stri.size(); i++){
			if (stri[i] != ' ' )break;
		}
		for (; i < stri.size(); i++){
			if (stri[i] > '9' || stri[i] < '0'){
				if (stri[i] == '+') {
					if (flag){
						ans = 0;
						break;
					}
					flag ++;
					continue;
				} else if (stri[i] == '-') {
					if (flag){
						ans = 0;
						break;
					}
					flag ++;
					isNe = 1-isNe;
					continue;
				}
				break;
			}
			if (!isNe){
				if (ans != 0 && MAXINT / ans < 10)return MAXINT;
				ans *= 10;
				if (ans > MAXINT - (stri[i] - '0'))return MAXINT;
				ans += stri[i] - '0';
			}else{
				if (ans<-1 && MININT / ans < 10)return MININT;
				ans *= 10;
				if (ans < MININT + (stri[i] - '0'))return MININT;
				ans -= stri[i] - '0';
			}
		}
		return ans;
    }
};

int main(){
	Solution s;
	printf("%d\n", -11/10);
	printf("%d\n", s.myAtoi("2147483647"));
	printf("%d\n", s.myAtoi("-2147483647"));
	printf("%d\n", s.myAtoi("-2147483648"));
	printf("%d\n", s.myAtoi("-2147483649"));
	printf("%d\n", s.myAtoi("           -2147483649"));
	printf("%d\n", s.myAtoi("           -1823121312"));
	printf("%d\n", s.myAtoi("           -18231213120"));
}
