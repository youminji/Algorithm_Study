/*
	[BOJ] 17413 단어 뒤집기 2
*/
#pragma warning (disable: 4996)
#include <queue>
#include <stack>
#include <cstdio>
using namespace std;


int main() {
	queue<char> q;
	stack<char> s;
	bool flag = 0;
	while (1) {
		char c;
		scanf("%c", &c);
		if (c == '\n') {
			while (!s.empty()) {
				q.push(s.top());
				s.pop();
			}
			break;
		}
		if (c == ' ') {
			while (!s.empty()) {
				q.push(s.top());
				s.pop();
			}
			q.push(' ');
		}
		else if (c == '<' || c=='>') {
			flag = !flag;
			while (!s.empty()) {
				q.push(s.top());
				s.pop();
			}
			q.push(c);
		}
		else {
			if (flag) {		//< 이후
				q.push(c);
			}
			else {
				s.push(c);
			}
		}
	}
	while (!q.empty()) {
		printf("%c", q.front());
		q.pop();
	}

	return 0;
}