#include <iostream>
using namespace std;

void mergeSort(int arr[], int l , int r);
void merge(int arr[], int l, int m, int r);

int main()
{
    int arr[] = {1,3,4,9,4,6,9,1,2,3,9,4,3,4};
    int n = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, n - 1);
    cout << "sorted array: ";
    for (auto i : arr) {
        cout << i << " "; 
    }
}

void merge(int arr[], int l, int m, int r)
{
    // get size of subarrays
    int s1 = m - l + 1;
    int s2 = r - m;

    // create subarrays using indexes
    int L[s1], R[s2];

    // fill subarrays
    for (int i = 0; i < s1; i++)
    {
        L[i] = arr[l + i];
    }
    for (int i = 0; i < s2; i++)
    {
        R[i] = arr[m + i + 1];
    }

    // merge subarrays into arr
    int le = 0, ri = 0, i = l;
    while (le < s1 && ri < s2)
    {
        if (L[le] <= R[ri])
        {
            arr[i] = L[le++];
        }
        else
        {
            arr[i] = R[ri++];
        }
        i++;
    }

    // fill rest of array in
    while (le < s1)
    {
        arr[i++] = L[le++];
    }

    while (ri < s2)
    {
        arr[i++] = R[ri++];
    }
}

void mergeSort(int arr[], int l, int r)
{
    if (l < r) {
        int mid = l + (r - l) / 2;
        mergeSort(arr, mid + 1, r);
        mergeSort(arr, l, mid);
        merge(arr, l, mid, r);
    }
}