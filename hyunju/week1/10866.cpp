#include<iostream>
#include <deque>
#include <string>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin >> n;
	deque<int> de;

	while(n--)
	{
		string s;
		cin >> s;
		if (s == "push_back")
		{
			int n ;
			cin >> n;
			de.push_back(n);
		}
		else if (s == "push_front")
		{
			int n ;
			cin >> n;
			de.push_front(n);
		}
		else if (s == "front")
			de.empty()? cout << -1 << "\n" : cout << de.front() << "\n";
		else if (s == "empty")
			de.empty()? cout << 1 << "\n": cout << 0 << "\n";
		else if (s == "back")
			de.empty()? cout << -1 << "\n": cout << de.back() << "\n";
		else if (s == "size")
			cout << de.size() << "\n";
		else if (s[0] == 'p')
		{
			if (s[4] == 'b')
			{
				if (!de.empty())
				{
					cout << de.back() << "\n"; de.pop_back();
				}
				else cout << -1 << "\n";
			}
			else if (s[4] == 'f')
			{
				if (!de.empty())
				{
					cout << de.front() << "\n"; de.pop_front();
				}
				else cout << -1 << "\n";
			}
		}
	}
	return 0;
}
