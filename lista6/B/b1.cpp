#include <bits/stdc++.h>
#include <numeric>  // Para usar std::gcd
using namespace std;

int n, a[105], maxx;
string s;

int main() {
    scanf("%d\n", &n);

    for (int i = 1; i <= n; i++) {
        maxx = -1;
        getline(cin, s);
        stringstream s1(s);
        int p = 0;
        while (s1 >> a[p]) ++p;
        
        for (int j = 0; j < p; j++) {
            for (int k = j + 1; k < p; k++) {
                maxx = max(maxx, gcd(a[j], a[k]));
            }
        }
        cout << maxx << endl;
    }
}
