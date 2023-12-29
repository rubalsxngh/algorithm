#include <iostream>
using namespace std;

int main() {
    int n;
    cout<<"please enter the size of array"<<endl;
    cin>>n;

    int nums[n];
    cout << "Enter " << n << " nums: "<<endl;
    int num;
    
    for(int i=0; i< n; i++) {
        cin>>num;

        nums[i]= num;
    }

    //implementing bubble sort

    for(int i=0; i< n; i++) {
        for(int j=i+1; j<n; j++) {
            if(nums[i]> nums[j]) {
                int temp= nums[i];
                nums[i]= nums[j];
                nums[j]= temp; //implemented swap
            }
        }
    }

    cout<<"sorted array is as follows"<<endl;

    for(int i=0; i<n; i++) {
        cout<<nums[i]<<' ';
    }

}