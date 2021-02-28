/*
	[BOJ] 1918 후위표기식
*/
#include <iostream>
#include <stack>
#include <vector>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	stack<char> s;
	vector<char> v;
	string str;
	cin >> str;

	for (int i = 0; i < str.size(); ++i) {
		if (str[i] == '(') {
			s.push(str[i]);
		}
		else if (str[i] == '*' || str[i] == '/') {
			if (!s.empty() && (s.top() == '*' || s.top() == '/')) {
				cout << s.top();
				s.pop();
			}
			s.push(str[i]);
		}
		else if (str[i] == '+' || str[i] == '-') {
			while(!s.empty()&& s.top()!= '(' ) {
				cout << s.top();
				s.pop();
			}
			s.push(str[i]);
		}
		else if (str[i] == ')') {
			while (s.top() != '(') {
				cout << s.top();
				s.pop();
			}
			s.pop();
		}
		else {
			cout << str[i];
		}
	}
	while (!s.empty()) {
		cout << s.top();
		s.pop();
	}
	return 0;
}