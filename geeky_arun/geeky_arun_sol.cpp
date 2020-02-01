#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	long int t;
	cin>>t;
	while(t--)
	{
		long long int n,i=0;
		cin>>n;
		long int power=0;
		
		while(power<n)
		{
			power+=pow(2,i);
			i++;
		}
		cout<<i<<endl;
	}
	
	return 0;
}