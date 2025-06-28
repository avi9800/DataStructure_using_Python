#ASCENDING ORDER

#Function for sorting using quicksort
def quicksort(arr, low, high):
    if low < high:
        pivot_index = find_pivot(arr, low, high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)
    return arr

#Function for finding pivot
def find_pivot(arr,low,high):
    pivot = arr[low]
    i=low
    j=high

    #Find the greatest and lowest number and swap
    while (i<j):

        #Keep on finding the smallest number than pivot
        while(arr[i]<=pivot and i<=(high-1)):
            i+=1
        
        #Keep on finding the greater number than pivot
        while(arr[j]>pivot and j>=(low+1)):
            j-=1
        #Swap the smaller and greater numbers
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]   
    #Swap and place the pivot at the correct place
    arr[low],arr[j]=arr[j],arr[low]
    return j


array = [4,2,7,0,1,6,9,8]
print(quicksort(array,0,len(array)-1))