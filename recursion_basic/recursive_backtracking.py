def printing(i):
    if i <= 0:
        print("--------------------")
        return
    else:
        print(i)
        printing(i-1)
        print(i)

printing(10)