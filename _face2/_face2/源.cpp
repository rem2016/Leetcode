#include <iostream>
#include <sstream>
#include <vector>
#include <math.h>

using namespace std;
int ma[1000][1000];

bool Find(int m, int n, const vector<int>& tx, const vector<int>& ty, const vector<int>& wx, const vector<int>& wy)
{
	// ������ɢ�ķ�ʽ��BFS���Ҳ�����Ļ��پ�ȷ�ж�һ���鵽����һ�����Ƿ����ͨ��
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < tx.size(); k++) {
				if ()
			}
		}
	}
}

int main()
{
	int m = 0;
	int n = 0;
	vector<int> tx;
	vector<int> ty;
	vector<int> wx;
	vector<int> wy;
	int num = 0;
	cin >> m;
	cin >> n;
	cin >> num;
	for (int i = 0; i < num; ++i) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		tx.push_back(x1);
		ty.push_back(y1);
		wx.push_back(x2);
		wy.push_back(y2);
	}
	cout << Find(m, n, tx, ty, wx, wy) << endl;
	return 0;
}