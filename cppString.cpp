//Date Started: 190823

#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a;
    string b;

    cin >> a >> b;

    int la = a.size();
    int lb = b.size();

    cout << la << " " << lb << endl;
    cout << a + b << endl;

    for (int i = 0; i < la; i++) {
        if (i == 0) {
            cout << b[0];
        } else {
            cout << a[i];
        }
    }

    cout << " ";

    for (int i = 0; i < lb; i++) {
        if (i == 0) {
            cout << a[0];
        } else {
            cout << b[i];
        }
    }
  
    return 0;
}
