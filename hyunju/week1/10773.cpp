#include <iostream>
#include <stack>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, m;
	stack <int> st;

	cin >> n;
	while(n--)
	{
		cin >> m;
		if (m == 0)
			st.pop();
		else
			st.push(m);
	}

	int sum = 0;

	while(!st.empty())
	{
		sum += st.top();
		//cout << sum << '\n';
		st.pop();
	}

	cout << sum;
	return 0;
}
