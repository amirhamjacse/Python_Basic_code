# write a python function to find the max of theree numbers

a = 23
b = 20
c = 43
def maxnum(a, b, c):
    if a>b and a>c:
        largest = a
    elif b>a and b>c:
        largest = b
    else:
        largest = c
        return largest
    



print(maxnum(a, b, c))