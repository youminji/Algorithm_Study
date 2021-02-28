/*
	[BOJ] 10773 Á¦·Î
*/
#pragma warning (disable: 4996)

#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	vector<int> s;
	int N = 0;
	cin >> N;
	while (N--) {
		int num = 0;
		cin >> num;
		if (num == 0) {
			s.pop_back();
		}
		else {
			s.push_back(num);
		}
	}
	int sum = 0;
	for (int i = 0; i < s.size(); ++i) {
		sum += s[i];
	}
	cout << sum << "\n";
	return 0;
}