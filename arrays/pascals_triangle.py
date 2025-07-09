def nth_element_of_pascal_triangle(row,column):
    n = row-1
    r = column-1
    rem = 1
    for i in range(r):
        rem = rem * (n-i)
        rem = rem/(i+1)
    
    print(f"Element at {row},{column} = {int(rem)}")


def print_Nth_row(row):
    values = "1"
    top = 1
    for i in range(1,row):
        top = (top * (row - i))/i
        values = values + " " + str(int(top))
    
    print(values)


def print_pascal_triangle(row):
    for i in range(row):
        print_Nth_row(i+1)

nth_element_of_pascal_triangle(5,3)
print_Nth_row(5)
print_pascal_triangle(6)
