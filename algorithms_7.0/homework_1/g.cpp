#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <numeric>
#include <map>
using ll = long long;
using namespace std;

int main() {
    // input
    int N, K, li, ci, len, ind_b, ind = 1;
    cin >> N >> K;
    vector<vector<pair<int, int>>> bricks(K + 1);
    vector<int> total(K + 1, 0);

    map<pair<int,int>, int> paths;

    for (int i = 0; i < N; ++i) {
        cin >> li >> ci;
        bricks[ci].push_back(make_pair(li, i + 1));  // кирпичи, цветом ci, длиной li и индексом i + 1

        paths[{ci, i + 1}] = li;

        total[ci] += li;
    }

    int mx_len = total[1];
    for (int c = 2; c <= K; c++) {
        if (total[c] != mx_len) {
            cout << "NO";
            return 0;
        }
    }

    // problem solving
    vector<vector<pair<int, int>>> bag(K + 1, vector<pair<int, int>>(5001, {-1, -1}));
    for (int j = 0; j < 5001; ++j) bag[0][j].first = 0;

    for (int i = 1; i < K + 1; ++i) {  // 50
        bag[i][0].first = 0; 
        bag[i][0].second = 0;
        paths[{i, 0}] = 1;
        for (int ind_brick = 0; ind_brick < bricks[i].size(); ++ind_brick) {  // 50
            len = bricks[i][ind_brick].first;
            ind_b = bricks[i][ind_brick].second;

            for (int j = (5000 - len); j > -1; --j) {  // 5000
                if (bag[i][j].first != -1 && bag[i][j + len].first == -1) {
                    bag[i][j + len].first = ind_b;  // сохраняем индекс кирпича
                    bag[i][j + len].second = ind_b;  // сохраняем индекс кирпича
                }    
            }
        }
        // делаем проверку можно ли оставить кирпичи
        for (int j = 0; j < 5001; ++j) {
            if (!(bag[i-1][j].first > -1 && bag[i][j].first > -1)) {
                bag[i][j].first = -1;
            }
        }
    }

    int q, last;
    for (int j = 1; j < 5001; ++j) {
        if (j == mx_len) break;
        if (bag[K][j].first > -1) {
            cout << "YES" << endl;
            for (int i = K; i > 0; --i) {
                q = j;
                last = bag[i][q].second;
                while (q - paths[{i, last}] > -1) {
                    cout << bag[i][q].second << " ";
                    q -= paths[{i, last}];
                    last = bag[i][q].second;
                }
            }
            return 0;
        }
    }

    cout << "NO";
    return 0;
}