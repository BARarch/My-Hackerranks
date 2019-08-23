//Date Started: 190822

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n;
    cin >> n;
    int y, x;
    set<int> s;
    for (int i = 0; i < n; i++) {
        cin >> y >> x;
        if (y == 1) {
            s.insert(x);
        }
        if (y == 2) {
            s.erase(x);
        }
        if (y == 3) {
            if (s.find(x) == s.end()) {
                cout << "No " << "\n";
            } else {
                cout << "Yes " << "\n";
            }
        }
    }   
    return 0;
}
