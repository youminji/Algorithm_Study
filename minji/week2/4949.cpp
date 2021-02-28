/*
	[BOJ] 4949 ±ÕÇüÀâÈù ¼¼»ó
*/

#pragma warning (disable: 4996)
#include <iostream>
#include <sstream>
#include <stack>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	while (1) {
		bool flag = true;
		stack<char> s;
		string str;
		getline(cin, str);
		if (str[0] == '.') {
			break;
		}
		for (int i = 0; i < str.size(); ++i) {
			if (str[i] == '[')
			{
				s.push('[');
			}
			else if (str[i] == ']') {
				if (!s.empty() && s.top() == '[') {
					s.pop();
				}
				else {
					flag = false;
					break;
				}
			}
			else if (str[i] == '(') {
				s.push('(');
			}
			else if (str[i] == ')') {
				if (!s.empty()&& s.top() == '(') {
					s.pop();
				}
				else {
					flag = false;
					break;
				}
			}
		}
		if (flag) {
			if (s.size()) {
				cout << "no\n";
			}
			else {
				cout << "yes\n";
			}
		}
		else {
			cout << "no\n";
		}
	}

	return 0;
}