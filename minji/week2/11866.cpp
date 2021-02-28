/*
	[BOJ] 11866 요세푸스 문제 0
*/
#include <iostream>
#include <queue>
#include <vector>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	queue<int> q;
	vector<int> v;
	int N, M,cnt=1;
	cin >> N >> M;
	
	for (int i = 1; i <= N; ++i) {
		q.push(i);
	}
	
	while (!q.empty()) {
		if (cnt % M == 0 && cnt!= 0) {
			v.push_back(q.front());
			q.pop();
		}
		else {
			int temp = q.front();
			q.pop();
			q.push(temp);
		}
		cnt++;
	}
	cout << "<";
	for (int i = 0; i < v.size(); ++i) {
		cout << v[i];
		if (i != v.size() - 1) {
			cout << ", ";
		}
	}
	cout << ">";
	

	return 0;
}