#include <iostream>
#include <queue>
using namespace std;

int main(int argc, char *argv[])
{
	ios_base::sync_with_stdio(false);
	int N, K;
	queue<int> q;
	cin >> N >> K;

	for (int i = 1; i <= N; i++)
		q.push(i);

	cout << "<";
	while (!q.empty()) 
	{
		for (int i = 0; i < K - 1; i++) 
		{
			q.push(q.front());
			q.pop();
		}

		cout << q.front();
		q.pop();

		if (!q.empty())
			cout << ", ";
	}
	cout << ">" << "\n";

	return 0;
}
