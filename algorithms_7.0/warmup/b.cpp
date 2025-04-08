#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using ll = long long;
using namespace std;


int main() {
    int n, m = 3;
    cin >> n;
    vector <vector <ll> > a(n);
    vector <ll> dp(n+1);
    for (int i = 0; i < n; ++i) {
        a[i].resize(m);
        for (int j = 0; j < m; ++ j) {
            cin >> a[i][j];
        }
    }
    dp[1] = a[0][0];
    if (n == 1) {
        cout << dp[1];
        return 0;
    } 
    dp[2] = min(dp[1] + a[1][0], a[0][1]);
    if (n == 2) {
        cout << dp[2];
        return 0;
    }
    for (int i = 3; i < n + 1; ++i) {
        dp[i] = min({dp[i-1] + a[i-1][0], dp[i-2] + a[i-2][1], dp[i-3] + a[i-3][2]});
    }
    // for (int i = 0; i < n + 1; ++i) {
    //     cout << dp[i] << " ";
    // }
    cout << dp[n];
    return 0;
}