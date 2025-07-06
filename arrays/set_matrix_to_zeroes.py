def bruteforce(arr):
    arr = arr.copy()
    m = len(arr)
    n = len(arr[0])
    #Change matrix value to -1 to retain zeros of question
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0: #Iterate and find the element which is zero
                #Mark the column as -1
                for c in range(m):
                    if arr[c][j] != 0: #If not zero mark the column as -1
                        arr[c][j] = -1
                #Mark the row as -1
                for r in range(n):
                    if arr[i][r] != 0: #If not zero mark the row as -1
                        arr[i][r] = -1
    
    #Change the values of -1 to 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == -1: #Change previously marked -1 to 0
                arr[i][j] = 0
    
    print(arr)

def better(arr):
    zeros = []
    m = len(arr)
    n = len(arr[0])
    #Find all the coordinates of zeros
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                zeros.append([i,j])
    print(zeros)

    #Perform operation of zero
    for zero in zeros:
        column = zero[0]
        row = zero[1]
        #mark the rows
        for r in range(n):
            arr[column][r] = 0
        
        #mark the rows
        for c in range(m):
            arr[c][row] = 0
    
    print(arr)

array = [[1,1,1],[1,0,1],[1,1,1]]#[[1,1,1,1],[1,0,0,1],[1,1,0,1],[1,1,1,1]]

better(array)
# [[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]
