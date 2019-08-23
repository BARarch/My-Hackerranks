//Date Started: 190822

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    vector<int> v;
    int num;
    for (int i = 0; i < n; i++) {
        cin >> num;
        v.push_back(num);
    }

    int i, j, k;
    cin >> i >> j >> k;
    v.erase(v.begin() + i - 1);
    v.erase(v.begin() + j - 1, v.begin() + k - 1);
    
    cout << v.size() << "\n";
    for (int i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
  
    return 0;
}
