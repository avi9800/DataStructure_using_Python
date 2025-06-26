def printing(i):
    if i <= 0:
        return
    else:
        printing(i-1)
        print(i)

printing(10)