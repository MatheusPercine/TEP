#include<bits/stdc++.h>
using namespace std;
#define ll __int64
#define mod 1000000007
#define pi (4*atan(1.0))
const int N=1e3+10,M=1e6+10,inf=1e9+10;

ll gcd(ll a,ll b){
    return b==0?a:gcd(b,a%b);
}

int main() {
    ll x,y,z,i,t;
    ll lcm=1;
    scanf("%lld%lld",&x,&y);
    for(i=0;i<x;i++)
    {
        scanf("%lld",&z);
        lcm=z*lcm/gcd(z,lcm);
        lcm%=y;
    }
    if(lcm==0)
    printf("Yes\n");
    else
    printf("No\n");
    return 0;
}