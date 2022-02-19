#include<bits/stdc++.h>
using namespace std;
bool cmp(vector<int> a, vector<int> b){
    float n1 = a[1]*1.0/a[0];
    float n2 = b[1]*1.0/b[0];
    return n1 > n2;
}
float knapsack(vector<vector<int>> v, int n, int val){
    sort(v.begin(), v.end(), cmp);
    float ans = 0;
    float weight = 0;
    for(int i=0; i<n; i++){
        if(weight + v[i][0] < val){
            weight += v[i][0];
            ans += v[i][1];
        }else{
            if(weight == val){
                break;
            }else{
                // cout << weight << " -<weight" << endl;
                float temp = 1 - (v[i][0] - (val - weight))*1.0/v[i][0];
                ans += v[i][1]*1.0*temp;
                break;
            }
        }
    }
    return ans;
}
int main(){
    int n;
    cout << "enter size of array ";
    cin >> n;
    cout << "enter weight and profit :" << endl;
    vector<vector<int>> v(n, vector<int> (2,0)); // weight, price
    for(int i=0; i<n; i++){
        cin >> v[i][0] >> v[i][1];
    }
    int val;
    cout << "enter max value of weight ";
    cin >> val;
    float value = knapsack(v, n, val);
    cout << value << endl;
}