#include<stdio.h>
#include<conio.h>
#include<bits/stdc++.h>

using namespace std;

int main(){
   vector<int>vres;
   int n;

    for(int i=0; i<10000000; i++){
     
            n = i^3 + 100*i + 5;
            vres.push_back(n);
    }

    cout<<vres.size();

}