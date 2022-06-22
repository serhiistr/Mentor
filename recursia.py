# def recursive(value):
#     print(value)
#     if value < 4:
#         recursive(value + 1)
#     print(value)
# recursive(1)

def recur(x):
    if x < 3:
        print(x)
        recur(x+1)
        print(x)
    return

recur(1)
