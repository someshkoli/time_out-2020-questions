#include<bits/stdc++.h>
#define ll long long int
#define pii pair<ll,ll>
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define ff first
#define ss second
#define M 1000005
#define mod 1000000007
#define inf LLONG_MAX
using namespace std;
vector<ll> prime(M,1);
int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	ll t,n,m,q,i,j,k,x,y,z;
	for(i=2;i*i<M;i++)
	{
		if(prime[i])
		{
			for(j=i*i;j<M;j+=i)
			{
				prime[j]=0;
			}
		}
	}
	
	cin>>t;
	while(t--)
	{
			k=0;
			cin>>n;
			ll ans=0;
			for(i=2;i<=n;i++)
			{	
				if(prime[i] && 2*i>n)
				ans++;
				else
				k=1;
			}
			cout<<ans+k<<"\n";
		
	}
}

// Name - Hemant Chowdhury
// Arise, Awake And Stop Not Till The Goal Is Reached!
// If I fail,I will stand again;If I win,I will move farther