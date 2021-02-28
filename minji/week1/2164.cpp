/*
	[BOJ] 2164 Ä«µå2
*/
#include <iostream>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	queue<int> q;
	int n = 0;
	cin >> n;

	for (int i = 1; i <= n; ++i) {
		q.push(i);
	}

	while (q.size() > 1) {
		q.pop();
		q.push(q.front());
		q.pop();
	}
	cout << q.front() << "\n";


	return 0;
}


