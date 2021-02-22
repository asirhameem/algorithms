#include <iostream>

using namespace std;

int main()
{
    int t;
    cout<< "How many elements you want to sort??" << endl;
    cin>> t;
    int nums[t];
    int n = 0;
    while(n < t)
    {
        cin>>nums[n];
        n++;
    }


    for(int i = 1; i < t; i++)
    {
        for(int k = 0; k < t-i-1; k++)
        {
            if(nums[k] > nums[k+1])
            {
                //int sw = nums[k];
                //nums[k] = nums[k+1];
                //nums[k+1] = sw;
                swap(nums[k],nums[k+1]);
            }
        }
    }
    int j = 0;

    while(j < t)
    {
        cout << nums[j] << " ";
        j++;
    }
}
