def brute_force(arr):
    arr = arr.copy()
    columns = len(arr)
    rows = len(arr[0])
    result = [[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            # Interchange items
            # new_column  = (n-1)-previous_row
            # new_row = previous column
            new_column = (rows-1)-i
            new_row = j
            result[new_row][new_column] = arr[i][j]
    
    for row in result:
        print(row)

def optimal(arr):
    arr = arr.copy()
    columns = len(arr)
    rows = len(arr[0])
    counter = 0
    for i in range(rows-1):
        for j in range(i+1,columns-1):
            counter +=1
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    print(counter)
    for j in range(columns): #Reverse each row of the transpose matrix
        arr[j].reverse()
    
    print("After 90 degree rotation")

    for x in arr:
      print(x)

array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for row in array:
    print(row)
optimal(array)

