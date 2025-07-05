def bruteforce(arr):
    length = []
    search = set(arr)
    for i in range(len(arr)):
        temp = []
        found = True
        temp.append(arr[i])
        x = arr[i]
        while found:
            x += 1
            if x not in search:
                found = False
            else:
                temp.append(x)

        if len(temp) == len(arr):
            print(arr)
            return
        if len(temp) > len(length):
            length = temp.copy()

    print("Maximum array - ",length)

def better(arr):
    arr.sort()
    longest = 0
    current_long = 0
    last_larger = -1
    for i in arr:
        if i-1 == last_larger:
            current_long+=1
            last_larger = i
        else:
            last_larger = i
            current_long = 0

        if current_long > longest:
            longest = current_long

def optimal(arr):
    if len(arr) == 1:
        return 0

    longest = 0
    arr = set(arr)
    for i in arr:
        count = 1
        x = i
        while x+1 in arr:
            count +=1
            x+=1
        longest = max(count,longest)
    print(longest)






arr = [102, 4, 100, 1, 101, 200, 201, 99, 1]
optimal(arr)
