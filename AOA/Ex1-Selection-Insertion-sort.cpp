#include <bits/stdc++.h>
using namespace std;

void traverse(int arr[], int n){
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }cout<<endl;
}
void insertionSort(int arr[], int n){
    for(int i=1; i<n; i++){
        traverse(arr, n);
        int j = i;
        while(j){
            if(arr[j] < arr[j-1]){
                swap(arr[j], arr[j-1]);
            }else{
                break;
            }
            j--;
        }
    }
}
void selectionSort(int arr[], int n){
    for(int i=0; i<n-1; i++){
        traverse(arr, n);
        int mini = INT_MAX;
        int minInd = i;
        for(int j = i; j<n; j++){
            if(arr[j] < mini){
                mini = arr[j];
                minInd = j; 
            }
        }
        swap(arr[i], arr[minInd]);
    }
}
int main()
{
    int n1;
    cin >> n1;
    int arr1[n1];
    for(int i=0; i<n1; i++){
        cin >> arr1[i];
    }
    insertionSort(arr1, n1);
    traverse(arr1, n1);
    int n2;
    cin >> n2;
    int arr2[n2];
    for(int i=0; i<n2; i++){
        cin >> arr2[i];
    }
    // int arr2[]={5, 4, 3, 2, 1}; int n2=5;
    selectionSort(arr2, n2);
    traverse(arr2, n2);

    return 0;
}
