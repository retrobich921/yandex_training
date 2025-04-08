#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using ll = long long;
using namespace std;


int dfs(string s, map<string, string>& tree, int cnt) {
    if (tree.find(s) != tree.end()) {
        return dfs(tree[s], tree, cnt+1);
    } else return cnt;
}


int main() {
    int n;
    bool flag;
    string s1, s2;
    cin >> n;
    vector <string> men;
    map <string, string> tree;
    for (int i = 0; i < n-1; ++i) {
        cin >> s1 >> s2;
        tree[s1] = s2;
        // проверка s1
        flag = true;
        for (auto x: men) {
            if (x == s1) {
                flag = false;
            }
        }
        if (flag) men.push_back(s1);
        // проверка s2
        flag = true;
        for (auto x: men) {
            if (x == s2) {
                flag = false;
            }
        }
        if (flag) men.push_back(s2);
    }
    sort(men.begin(), men.end());

    for (auto x: men) {
        cout << x << " " << dfs(x, tree, 0) << "\n";
    } 


    return 0;
}