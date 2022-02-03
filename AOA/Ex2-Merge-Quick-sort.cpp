#include <iostream>

using namespace std;

void traverse(int arr[], int n){
    for(int i=0; i<n; i++){
        cout << arr[i] << " ";
    }
    cout << endl;
}

void merge(int arr[], int low, int mid, int high){
    int temp[high - low + 1];
    // cout << "size=" << (high-low+1)<< endl;
    mid = mid + 1;
    int l = low, m = mid, h = high;
    // cout << low << " " << mid << " " << high << endl;
    int i=0;
    while(l<mid && m<=high){
        if(arr[l] > arr[m]){
            // cout << "low>mid mid="<<m <<endl;
            temp[i++] = arr[m++];
        }else{
            // cout << "low<mid low="<<l <<endl;
            temp[i++] = arr[l++];
        }
    }
    while(l<mid){
        // cout << "inside norml while low="<<l <<endl;
        temp[i++] = arr[l++];
    }
    while(m<=high){
        // cout << "inside norml while mid="<<m <<endl;
        temp[i++] = arr[m++];
    }
    // cout<<"temp=";
    // traverse(temp, high - low + 1);
    int k = 0;
    for(int j=low; j<=high; j++){
        arr[j] = temp[k++];
    }
    // traverse(arr, 5);
}

void mergeSort(int arr[], int low, int high){
    if(low < high){
        int mid = (high + low)/2;
        mergeSort(arr, low, mid);
        mergeSort(arr, mid+1, high);
        merge(arr, low, mid, high);
    }
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }
    // int arr[5] = {5,4,3,2,1};
    // int n = 5;
    traverse(arr, n);
    mergeSort(arr, 0, n-1);
    traverse(arr, n);
    return 0;
}
