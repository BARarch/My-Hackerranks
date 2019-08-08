#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, q;
    scanf("%d %d", &n, &q);
    std::vector<int> a[n];           // The golden line, an array of vectors of ints

    int k;
    for(int i = 0; i < n; i++) {
        cin >> k;
        int num;
        for(int j = 0; j < k; j++) {
            cin >> num;
            a[i].push_back(num);
        }
    }

    int i;
    int j;
    for(int k = 0; k < q; k++) {
        scanf("%d %d", &i, &j);
        cout << a[i][j] << "\n";
    }

    return 0;
}