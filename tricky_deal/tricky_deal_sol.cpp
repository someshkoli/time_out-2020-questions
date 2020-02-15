#include<bits/stdc++.h>
#define mod 1000000007
#define lim 1000000000000000007
#define pb push_back
#define sq(a) ((a)*(a))
#define all(v) v.begin(),v.end()
using namespace std;
typedef long long int ll;
typedef pair<int,int> pi;
const int N = (int)1e5+5;
ll solve1(ll a) {
    ll lo=1,hi=60,mi;
    while (lo<hi) {
        mi = 1+(lo+hi)/2;
        ll g = mi*a-(((ll)1)<<mi)+1;
        if (g>0) lo=mi;
        else hi=mi-1;
    }
    return lo;
}
ll solve2(ll a) {
    ll lo=1,hi=60,mi;
    while (lo<hi) {
        mi = 1+(lo+hi)/2;
        ll g = a-(((ll)1)<<(mi-1));
        if (g>0) lo=mi;
        else hi=mi-1;
    }
    return lo;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T;
    ll a;
    cin>>T;
    while (T--) {
        cin>>a;
        cout<<solve1(a)<<" "<<solve2(a)<<"\n";
    }
}
