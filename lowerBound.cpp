//Date Started: 190822

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin >> n;
    vector<int> v;
    int num;
    for (int i = 0; i < n; i++) {
        cin >> num;
        v.push_back(num);
    } 

    int m;
    cin >> m;
    int q;
    vector<int>::iterator lo;
    for (int i = 0; i < m; i++) {
        cin >> q;
        lo = lower_bound(v.begin(), v.end(), q);
        if (*lo == q) {
            cout << "Yes ";
        } else {
            cout << "No ";
        }
        cout << lo - v.begin() + 1 << "\n";
    } 
    return 0;
}
