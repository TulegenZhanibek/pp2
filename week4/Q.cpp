#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n; 
    char k = '.';

    for(int i = 0; i < n; i++){
        for(int j = 0; j < (n * 2) - 1; j++){

            if(i + j < n - 1){
                cout << k;
            }
            else if(j - i > n - 1){
                cout << k;
            }
            else {
                cout << "*";
            }
        }
        cout << endl;
    }
}