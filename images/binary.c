#include<stdio.h>
int arr[]={1,2,3,4,5,6,7,8,9};
void binarySearch(int arr[],int low,int high, int key){
    if(low<=high){
    int mid =(low+high)/2;
    if(arr[mid]==key)
    printf("value is at index %d\n",mid);
     if(key<arr[mid])
    
    binarySearch(arr,low,mid-1,key);
    if(key>arr[mid])
    
    binarySearch(arr,mid+1,high,key);
    } 
    else{
        printf("ELement is not present in array");
    }

}
int main(){
    binarySearch(arr,0,8,9);


}
