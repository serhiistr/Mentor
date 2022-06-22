def rec(x):
    if x < 4:
        print(x)
        rec(x+1)
    return


rec(3)
