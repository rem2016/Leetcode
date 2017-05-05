#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>
#include <cstring>


using namespace std;

int Find(int n)
{
	int flag[110];
	if (n <= 2)return 0;
	memset(flag, 0, sizeof(flag));
	for (int i = 1; i <= n; i++)
		flag[i] = n - i;
	for (int i = n - 2; i >= 1; i--) {
		for (int j = i + 1; j < n; j++) {
			if (j - i < flag[j]) {
				flag[i] = j - i;
				break;
			}
		}
	}
	if (flag[1] == n - 1)
		return 0;
	return flag[1];
}

/*
		2		0
		3		1
		4		
*/
int main()
{
	int n = 0;
	cin >> n;
	cout << Find(n) << endl;
	getchar();
	getchar();
	return 0;
}