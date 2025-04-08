#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using ll = long long;
using namespace std;


int main() {
    int n;
    cin >> n;
    vector <int> a(n);
    for (auto& x: a) {
        cin >> x;
    }
    sort(a.begin(), a.end());
    vector<int> q;
    for (int i=1; i < n; ++i) {
        q.push_back(a[i]-a[i-1]);
    }
    vector<int> dp={q[0], q[0]};
    for (int i=1; i < n-1; ++i) {
        dp.push_back(min(dp[i], dp[i-1]) + q[i]);
    }
    cout << dp[n-1];
    return 0;
}