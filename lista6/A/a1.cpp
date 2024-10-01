#include <iostream>
#include <cmath>
using namespace std;

long long ComputeS(long long K){
    long long S = 0;
    for (long long p = 2; p*p <= K; ++p){
        while (K % p == 0){
            S += p;
            K /= p;
        }
    }

    if (K> 1){
        S += K;
    }

    return S;
}

int main(){
    long long K;
    while(cin>>K) {
        cout << ComputeS(K) << endl;
    }
}