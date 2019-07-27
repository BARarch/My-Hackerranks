#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    int nums[n];
    for (int i = n - 1; i >= 0 ; i--) {
        cin >> nums[i];
    }
    for (int i = 0; i < n; i++) {
        cout << nums[i];
        cout << " ";
    }
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
