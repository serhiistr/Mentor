#
#
# def recursive(value):
#     print(value)
#     if value < 4:
#         recursive(value + 1)
#     print(value)
#
#
# recursive(1)

print("-------------")


def recur(x):
    if x < 4:
        print(x)
        recur(x+1)
        print(x)


recur(1)
