#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, m, t;
    cin >> n >> m;
    int a[n][m];

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    cin >> t;
    
    int max = a[0][0];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            
            if(a[i][j] > max){
                max = a[i][j];
            }
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            
            if(max > t){
                cout << "Penalty!";
                return 0;
            }
            else {
                cout << "No penalty for today.";
                return 0;
            }
        }
    }
}