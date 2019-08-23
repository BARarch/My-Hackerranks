//Date Started: 190822

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int get_grade(map<string, int> book, string name){
    map<string, int>::iterator itr = book.find(name);
    if (itr == book.end()) {
        return 0;
    } else {
        return itr -> second;
    }
}

int main() {
    int n;
    cin >> n;
    int query, y;
    string x;
    map<string, int> grades;
    for (int i = 0; i < n; i++) {
        cin >> query >> x;
        switch (query) {
            case 1:
                cin >> y;
                int tempGrade;
                tempGrade = get_grade(grades, x);
                //cout << "TempGrade " << tempGrade << endl;
                grades.erase(x);
                grades.insert(make_pair(x, (tempGrade + y)));
                break;
            case 2:
                grades.erase(x);
                break;
            case 3:
                cout << get_grade(grades, x) << endl;
                break;
        }
    }
    return 0;
}
