def optimal(arr,value):
    start, end = 0,0
    array = []
    sum_value = arr[0]
    while (end<len(arr)):
        if sum_value == value:
            if ((end-start)+1) > len(array):
                array = arr[start:end+1]
            end+=1
            if end < len(arr):
                sum_value += arr[end]
        if sum_value > value:
            sum_value -= arr[start]
            start+=1        
        if sum_value < value:
            end += 1
            if end < len(arr):
                sum_value += arr[end]
    
    print(array)


arr = [1,2,3,1,1,1,7,1,2]
value = 3
optimal(arr, value)
