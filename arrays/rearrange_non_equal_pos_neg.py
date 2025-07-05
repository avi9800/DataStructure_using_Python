def optimal(arr):
    pos_pointer = 0
    neg_pointer = 0
    count = 0

    # Let's take negatives
    for i in arr:
        if i < 0:
            count+=1
    
    #Check whether number of -ve or +ve is less and assign it count
    count = min(count, (len(arr)-count))
    
    result = [0] * len(arr)
    pointer = 0
    fill_in = (2*count)

    while (pos_pointer < count or neg_pointer < count or pointer < len(arr)):
        if arr[pointer] >= 0 and pos_pointer < count:  #First checks if all positives are filed
            result[2*pos_pointer] = arr[pointer]
            pos_pointer +=1
        elif pos_pointer >= count and arr[pointer] >= 0 and fill_in < len(arr): #Fill rest of the positive items after the decided space
            result[fill_in] = arr[pointer]
            fill_in+=1

        if arr[pointer] < 0 and neg_pointer < count: #First checks if all positives are filed
            result[2*neg_pointer+1] = arr[pointer]
            neg_pointer+=1
        elif neg_pointer >= count and arr[pointer] < 0 and fill_in < len(arr):
            result[fill_in] = arr[pointer]
            fill_in+=1
        
        print(count,pointer,result, pos_pointer, neg_pointer, fill_in)
        pointer+=1


arr = [1,-2,4,5,7,6,-8,-9]
optimal(arr)

