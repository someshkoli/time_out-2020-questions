# include<iostream>
using namespace std;
int main()
{
    int N,i,sum=0;  //N as an int
    int arr[100000];
    cin>>N;  //Entering the value of N
 
    for(i=0;i<N;i++){
       cin>>arr[i];} //Entering the value in array
 
    for(i=0;i<N;i++){
        sum=sum^arr[i];  //Logical value
    }
 
    if(sum==0)
        cout<<"JASBIR";  //Output the Name of winner
    else
        cout<<"AMAN";
 
    return 0;
}