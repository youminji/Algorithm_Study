#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n; cin >> n;
	queue<int> q;
	while(n--)
	{
		string s;
		cin >> s;
		//if (strcmp(s, "push"))
		if (s == "push")
		{
			int num; cin >> num;
			q.push(num);
		}
		else if (s == "pop")
		{
			if (q.empty()) cout << -1 << '\n';
			else
			{
				cout << q.front() << '\n';
				q.pop();
			}

		}
		else if (s == "front")
		{
			if(q.empty()) cout << -1 << '\n';
			else cout << q.front() << '\n';
		}
		else if (s == "back")
		{
			if(q.empty()) cout << -1 << '\n';
			else cout << q.back() << '\n';
		}
		else if (s == "size")
			cout << q.size() << '\n';
		else if (s == "empty")
		{
			if (!q.empty()) cout << 0 << '\n';
			else cout << 1 << '\n';
		}
	}
	return 0;
}