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


#define ROW(x, y)((y))
#define COL(x, y)((x))
#define GON(x, y)(((x) / 3) + (((y)/ 3) * 3))
class Solution {
public:
	bool isValidSudoku(vector<vector<char>>& board) {
		int row[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		int col[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		int gon[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				char v = board[i][j];
				if (v == '.') continue;
				int mask = (1 << (v - '0'));
				if ((mask & row[ROW(j, i)]) || (mask & col[COL(j, i)]) || (mask & gon[GON(j, i)])) {
					return false;
				}
				row[ROW(j, i)] |= mask;
				col[COL(j, i)] |= mask;
				gon[GON(j, i)] |= mask;
			}
		}
		return true;
	}
};