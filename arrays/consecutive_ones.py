def consecutive_ones(arr):
  check = 0
  count = 0
  for i in arr:
    if i == 1: #Check if the number is 1
      count +=1 #Increment the counter
      if count > check: #If the next consecutive ones is more than previous store it
        check = count
    else: #Reset the counter once the consecutive ones ends
      count = 0
  
  return check

arr = [1,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0]
print(consecutive_ones(arr))
