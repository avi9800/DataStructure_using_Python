def recursion(a , b):
    if b == 0:
        return
    else:
        print(f"{a} - {b}")
        recursion(a,b-1)



def main():
    recursion("Hellworld", 10)



main()