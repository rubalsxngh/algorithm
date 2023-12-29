/*          BUBBLE SORT
Interesting Fact : Bubble sort as a name came from the idea of bubble form in 
the glass of soda that forms in the bottom of the soda glass and traverse to the 
top of the glass just that we sort the last element first in the array and start
from the last element to the first element!
*/
#include<bits/stdc++.h>     //header file
using namespace std;

void swap(int &a, int &b) { //swap function to swap two elements
    int temp = a;
    a = b;
    b = temp;
}
int main() {
    int number; //number of element in an array
    cout<<"Enter the size of an array"<<endl;
    cin>>number;
    vector<int> arr;    //decalring a vector arr
    cout<<"Enter the elements of an array one by one"<<endl;
    for(int i=0;i<number;i++)
    {
        int element;
        cin>>element; // taking elements of an array by user one by one
        arr.push_back(element); // pushing it back to the arr vector
    }

    cout<<"Array before Sorting"<<endl;
    
    for(int i=0;i<number;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;

    // we will start sorting from the last element
    for(int i=0;i<number-1;i++)//taking number-1 because we are taking in inner loop j where it is incremented by 1
    {
        for(int j=0;j<number-i-1;j++)//taking number-i-1 because after every i iteration the last i elements will be sorted
        {
            if (arr[j] > arr[j+1]) {
                // Swap if the element found is greater than the next element
                swap(arr[j], arr[j + 1]);
            }
        }
    }
    cout<<"Array after Sorting"<<endl;
    
    for(int i=0;i<number;i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;

}