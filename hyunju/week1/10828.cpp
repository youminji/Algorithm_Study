#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	stack<int> st;
	cin >> n;
	while(n--)
	{
		string str;
		cin >> str;
		if (str == "push")
		{
            int c;
			cin >> c;
			st.push(c);
		}
		else if (str == "top")
		{
			if (st.empty())
				cout << -1 << '\n';
			else
				cout << st.top() << '\n';
		}
		else if (str == "size")
			cout << st.size() << '\n';
		else if (str == "pop")
		{
			if(!st.empty())
			{
				cout << st.top() << '\n';
				st.pop();
			}
			else
			{
				cout << -1 << '\n';
			}
		}
		else if (str == "empty")
		{
			cout << st.empty() << '\n';
		}
	}
	return 0;
}