#include <iostream>

using namespace std;


int Partition(int nums[],int low, int high)
{
    int pivot = nums[high];
    int lowIndex = low-1;
    for(int j = 0; j < high; j++)
    {
        if(nums[j] <= pivot)
        {
            lowIndex++;
            swap(nums[lowIndex],nums[j]);
        }
    }

}

int QuickSort(int nums[], int low, int high)
{
    if(low < high)
    {
        int pi = Partition(nums,low,high);
        QuickSort(nums,low,pi-1);
        QuickSort(nums,pi+1,high);
    }
}

int main()
{
    int t;
    cout << "How many elements you want to deal with ?" << endl;
    cin >> t;
    int numbers[t];
    for(int l = 0; l < t; l++)
    {
        cin >> numbers[l];
    }

    QuickSort(numbers,0,t-1);

    for(int k = 0; k < t; k++)
    {
        cout << numbers[k] << " ";
    }
}
