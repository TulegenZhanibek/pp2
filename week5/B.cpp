#include <bits/stdc++.h>
using namespace std;

int main(){
    int i;
    string s;
    cin >> s;
    for(int i = 0; i < s.size(); i++){
        
        if(s[i] >= 'a' && s[i] <= 'z'){
            s[i] -= 32;
        }
        cout << s[i];
    }
}