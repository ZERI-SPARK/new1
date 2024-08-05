#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define fast()                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define mklsa()       \
    fast();        \
    ll t;          \
    std::cin >> t; \
    while (t--)
#define input(v, n)             \
    for (int i = 0; i < n; i++) \
        cin >> v[i];
#define all(v) v.begin(), v.end()
#define nline "\n"
#define INF INT_MAX
#define MOD 1000000007

vector<int> primes;

void prime() {
    int n = 2;
    vector<int> temp(1000001, 0);
    while (n * n <= 1000000) {
        if (temp[0] == 0) {
            for (int i = 2 * n; i < 1000001; i += n) {
                temp[i] = 1; 
            }
        }
        n += 1;
    }

    for(int i = 2; i < 1000001; ++i)
        if (temp[i] == 0)
            primes.push_back(i);
}

int main()
{   
    prime();
    mklsa() {
        int n, ans;
        cin >> n;
        vector<int> v(n);
        input(v, n);
        
        for (int a : primes) {
            bool div = false;
            
            for (int x : v) {
                if(x % a == 0) {
                    div = true;
                    break;
                }
            }

            if (!div) {
                ans = a;
                break;
            }
        }

        cout << ans << nline;
    }
}
