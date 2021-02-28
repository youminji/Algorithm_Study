#include <iostream>
#include <queue>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;

	while(n--)
	{
		queue<pair<int, int>> q;
		priority_queue<int> pq;
		int papper, idx, cnt = 0;
		cin >> papper >> idx;
		for (int i = 0; i < papper; i++)
		{
			int pri;
			cin >> pri;
			q.push({i, pri});
			pq.push(pri);
		}
		while(!q.empty())
		{
			int nidx = q.front().first;
			int npri = q.front().second;
			q.pop();

			if (pq.top() == npri)
			{
				pq.pop(); cnt ++;
				if (nidx == idx)
				{
					cout << cnt << '\n'; break;
				}
			}
			else
				q.push({nidx, npri});
		}
	}
	return 0;
}
