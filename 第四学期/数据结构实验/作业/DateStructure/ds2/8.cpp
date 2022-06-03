#include<iostream>
#include<string>
using namespace std;

int main() {
	string s1;

	getline(cin, s1);
	for (int i = 0; i < s1.size(); i++) {
	s1[i] = tolower(s1[i]);
	}

	string a, b;
	while(getline(cin, a)) {
		b = a;
		for (int i = 0; i < b.size(); i++) {
			b[i] = tolower(b[i]);
		}
		int t = b.find(s1, 0);
		while (t != string::npos) {
			a.erase(t, s1.size());
			b.erase(t, s1.size());
			t = b.find(s1, 0);
		}
		t = b.find(" ", 0);
		while (t != string::npos) {
			a.erase(t, 1);
			b.erase(t, 1);
			t = b.find(" ", 0);
		}
		cout << a << endl;
	}
	return 0;
}
