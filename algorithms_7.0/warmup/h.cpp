#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using ll = long long;
using namespace std;

bool search(vector<int>& arr, int& x) {
    for (int i = 0; i < arr.size(); ++i) {
        if (arr[i] == x) {
            return true;
        }
    }
    return false;
}

string add(vector<int>& arr, int& x) {
    if (search(arr, x)) {
        return "ALREADY";
    } else {
        arr.push_back(x);
        return "DONE";
    }
}

void print(vector<int>& arr) {
    for (int i = 0; i < arr.size(); ++i) {
        for (int j = 0; j < i; ++j) {
            cout << ".";
        }
        cout << arr[i] << "\n";
    }
}


int main() {
    string command;
    int value, x;

    vector<int> a;

    while (getline(cin, command)) {
        if (command.substr(0, 3) == "ADD") {
            value = stoi(command.substr(4));
            cout << add(a, value) << endl;
        } 
        else if (command.substr(0, 6) == "SEARCH") {
            value = stoi(command.substr(7));
            if (search(a, value)) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        } 
        else if (command == "PRINTTREE") {
            print(a);
        }
    }

    return 0;
}