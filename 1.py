#substruction
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
def add(fname, snum):
    result = x + y   
    return result

def sub(fname, snum):
    result = x - y   
    return result

def mul(fname, snum):
    result = x * y   
    return result

def divi(fname, snum):
    result = x / y   
    return result

def expo(fname, snum):
    result = x ** y   
    return result

def sub(fname, snum):
    result = x // y   
    return result

def mod(fname, snum):
    result = x % y   
    return result


print("Addition result" ,add(x, y))
print("Substraction result"  ,sub(x, y))
print("Multiplication result"  ,mul(x, y))
print("Divition result"  ,divi(x, y))
print("Exponation result"  ,expo(x, y))
print("Modulas result" , mod(x, y))


