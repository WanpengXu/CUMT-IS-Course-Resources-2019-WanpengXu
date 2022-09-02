#include <iostream>
using namespace std;
int main() {
    int T;
    int n = 500;
    cin >> T;
    while (T--)
    {
        n++;
        cout << "第" << n << "次" << endl;
        int v = 1, s = 0;
        int v2 = 1, s2 = 0;
        for (int i = 0; i < n; i++) {
            s = (s + v) % 10000;
            v += 2;

            s2 += v2;
            v2 += 2;
        }
        cout << s << endl;
        cout << s2 % 10000 << endl;
    }
    return 0;
}