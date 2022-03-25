#include<bits/stdc++.h>
using namespace std;
int helper(string s1, string s2, int n, int m, vector<vector<int>> dp){
        if(s1[n] == '\0' || s2[m] == '\0'){
            return 0;
        }
        if(dp[n][m] != 0){
            return dp[n][m];
        }
        if(s1[n] == s2[m]){
            return dp[n][m] = 1 + helper(s1, s2, n+1, m+1, dp);
        }else{
            return dp[n][m] = max(helper(s1, s2, n, m+1, dp), helper(s1, s2, n+1, m, dp));
        }
    }
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.length(), vector<int> (text2.length(), 0));
        return helper(text1, text2, 0, 0, dp);
    }
int main(){
    string s1; string s2;
    cin >> s1 >> s2;
    cout << longestCommonSubsequence(s1, s2);
}