global arr
arr = [1,2,3,4,5]
def reverse(l, r):
    if l>r or len(arr) <=1:
        return
    reverse(l+1,r-1)
    t = arr[l]
    arr[l] = arr[r]
    arr[r] = t

def main(arr):
    reverse(0,len(arr)-1)

main(arr)
print(arr)