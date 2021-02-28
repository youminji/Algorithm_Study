/*
	[BOJ] 10828 Ω∫≈√
*/
#include <iostream>
#include <stack>
using namespace std;

int main() {
	stack<int> s;
	int N = 0;
	cin >> N;
	while (N--) {
		string cmd;
		int num = 0;
		cin >> cmd;
		if (cmd == "push") {
			cin >> num;
			s.push(num);
		}
		else if (cmd == "pop") {
			if (s.empty() == 1) {
				cout << "-1\n";
			}
			else {
				cout<<s.top()<<"\n";
				s.pop();
			}
		}
		else if (cmd == "size") {
			cout << s.size()<<"\n";
		}
		else if (cmd == "empty") {
			cout << s.empty() << "\n";
		}
		else if (cmd == "top") {
			if (s.empty() == 1) {
				cout << "-1\n";
			}
			else {
				cout << s.top() << "\n";
			}
		}
	}
	return 0;
}