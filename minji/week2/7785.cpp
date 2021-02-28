/*
	[BOJ] 7785 회사에 있는 사람
*/
#include <iostream>
#include <map>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	map< string, string> m;
	int n = 0;
	cin >> n;
	while (n--) {
		string name, door;
		cin >> name;
		cin >> door;
		if (door == "leave") {
			map<string, string>::iterator it = m.find(name);
			m.erase(name);
		}
		else {
			m.insert(make_pair(name, door));
		}
	}
	for (auto it = m.end(); it!=  m.begin(); it--  )
	{
		if (it != m.end())
		{
			cout << it->first << "\n";
		}
	}
	auto it = m.begin();
	cout << it->first << "\n";
	
	
	return 0;
}