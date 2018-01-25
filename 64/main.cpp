#include <queue>
#include <string.h>
#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

struct Node{
    int x, y, step;
    Node(int x_, int y_, int step_):x(x_),y(y_),step(step_){}
    friend bool operator < (const Node& a, const Node& b){
        return a.step > b.step;
    }
};

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0)
            return 0;
        int n = grid.size(), m = grid[0].size();
        vector<vector<int>> buff(n, vector<int>(m, 2147483647));
        priority_queue<Node> que;
        que.push(Node(0, 0, grid[0][0]));
        buff[0][0] = grid[0][0];
        while(!que.empty()){
            Node top = que.top();
            que.pop();
            if (top.step > buff[top.x][top.y])
                continue;
            if (top.x + 1 < n){
                saveResult(top.x + 1, top.y, top.step, grid, que, buff);
            } if (top.y + 1 < m){
                saveResult(top.x, top.y + 1, top.step, grid, que, buff);
            }
            if (top.x == n - 1 && top.y == m - 1)
                break;
        }
        return buff[n-1][m-1];
    }

private:
    void saveResult(int x, int y, int step, vector<vector<int>>& grid, priority_queue<Node>& que, vector<vector<int>>& buff){
        int last_v = buff[x][y];
        int this_step = grid[x][y] + step;
        if (this_step >= last_v)
            return;
        buff[x][y] = this_step;
        que.push(Node(x, y, this_step));
    }
};

void assert_ans(vector<vector<int> > input, int cor){
    Solution s;
    auto ans = s.minPathSum(input);
    if (ans != cor){
        cout<<cor<<endl;
    }
}

int main(){
    assert_ans(vector<vector<int> > {
        {0, 1, 2}
    }, 3);

    assert_ans(vector<vector<int> > {
        {0, 0, 2}
    }, 2);

    assert_ans(vector<vector<int> > {
        {1, 0, 0},
        {0, 0, 0}
    }, 1);

    assert_ans(vector<vector<int> > {
        {0},
    }, 0);

    assert_ans(vector<vector<int> > {
        {2},
    }, 2);
    getchar();
}