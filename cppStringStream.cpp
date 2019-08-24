//Date Started: 190823

#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	stringstream ss(str);
    vector<int> nums;
    int x;
    char ch;
    while (!ss.eof()) {
        ss >> x;
        nums.push_back(x);
        ss >> ch;
    } 


    return nums;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
