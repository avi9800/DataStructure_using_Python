array = [1,2,3,4,5,6]

def rotate(arr, rotation_direction):
    
    arr = arr.copy()
    if len(array) <= 1:
        return array

    #Left rotation by one key    
    if rotation_direction == "Left":
        temp = arr[0]  #Store first element
        for i in range(1,len(arr)): #Shift all elements of array by one
            arr[i-1] = arr[i]
        
        arr[len(arr)-1] = temp #Storing the first element at last place

        print("Array rotated by on key to the left - ",arr)
    
    elif rotation_direction == "Right":
        temp = arr[len(arr)-1]  #Store last element
        for i in range(len(arr)-1,0,-1): #Shift all elements of array by one
            arr[i] = arr[i-1]
        
        arr[0] = temp  #Storing last element at first place

        print("Array rotated by on key to the right - ",arr)


rotate(array, "Left") #Rotating to left
rotate(array, "Right") #Rotating to right

