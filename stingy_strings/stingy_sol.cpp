#include<bits/stdc++.h>
using namespace std;
int gcd(int a, int b)
{
    if (a == 0 || b == 0)
       return 0;
    if (a == b)
        return a;
    if (a > b)
        return gcd(a-b, b);
    return gcd(a, b-a);
}
int main()
{
	int t;
	int n;
	float k;
	cin>>t;
	while(t--)
	{
	cin>>n>>k;
	char s[n];
	for(int i=0;i<n;i++)
	{
	cin>>s[i];
	}
	int a=n;
	int b=0;
	
	for(int i=0;i<n;i++)
	{
	if(s[i]-96>2*k)
	{
    a=a-2;
	b=b+s[i]-96;	
	}	
	}
	int num=a*k+b;
	int den=k;
	int dividend=gcd(num,den);
	cout<<num/dividend<<" "<<den/dividend;
	cout<<'\n';
	}
	return 0;
}