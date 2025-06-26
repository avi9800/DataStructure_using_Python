def check(arr, i):
    if i > (len(arr)-1)//2:
        return True
    
    if arr[i] != arr[len(arr)-i-1]:
        return False

    return check(arr,i+1)

def main():
    arr = "ADDA"
    res = check(list(arr),0)
    print(res)

main()