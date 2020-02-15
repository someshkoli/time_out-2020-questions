#include<bits/stdc++.h>
#define _max 1000100
#define ll long long
using namespace std;


char str[_max];
pair<int, int> cnt[_max];

int main(int argc, const char *argv[]){
	str[0] = '0';
	//gets(str+1);
	scanf("%s", str + 1);
	int n = strlen(str + 1);
	//int n = strlen(str) - 1;
	cnt[0] = make_pair(0,0);
	int a = 0, b = 0, c = 0;
	for(int i = 1; i <=n; i++){
		if(str[i] == 'A'){
			a += 1;
		}
		if(str[i] == 'B'){
			b += 1;
		}
		if(str[i] == 'C'){
			c += 1;
		}
		cnt[i] = make_pair(b-a, c-a);
	}
	ll ans = 0, k = 0;
	pair<int, int> last(-1000000000, -1000000000);
	sort(cnt, cnt+n+1);
	for(int j = 0; j <= n; j++){
		if(cnt[j] != last){
			last = cnt[j];
			k = 0;
		}
		ans += k;
		k += 1;
	}
	cout << ans << endl;

	return 0;
}