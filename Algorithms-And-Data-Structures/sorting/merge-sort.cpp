#include <vector>
#include <iostream>
using namespace std;

void merge(vector<int> &arr, int l, int m, int r)
{
    if (l >= r)
        return;
    int size = r - l + 1, k = 0, i = l, j = m + 1; // i, j -> left right array start indexes respectively
    vector<int> sorted(size, 0);
    while (i <= m && j <= r) // compare two ararys
        sorted[k++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
    while (i <= m) // fill left over
        sorted[k++] = arr[i++];
    while (j <= r)
        sorted[k++] = arr[j++];
    for (int i = 0; i < size; i++) // copy sorted back into array
        arr[i + l] = sorted[i];
}

void mergeSort(vector<int> &arr, int l, int r)
{
    if (l >= r)
        return;
    int mid = l + (r - l) / 2;
    mergeSort(arr, mid + 1, r);
    mergeSort(arr, l, mid);
    merge(arr, l, mid, r);
}

int main()
{
    vector<int> arr = {0, 3, 2, 9, 0, 4, 2, -4, 2, 3, 7, 1, 1};
    mergeSort(arr, 0, arr.size() - 1);
    cout << "sorted array is: ";
    for(auto n : arr) {
        cout << n << " ";
    }
}