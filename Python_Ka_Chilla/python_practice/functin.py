def greet_user():
    print("Hello!")
    print("Welcome to Python")

def aoa(name):
    print(f"Assalam o Alaikum! kaifa haluk? {name}")


def square(num):
    return num*num

# Recursion function

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)



#lambda function
x = lambda a: a+10

xAdd = lambda a,b: a+b
print(xAdd(5,6),"\n")

xMult = lambda a,b: a*b
print(xMult(5,6))

# print(x(4))

# print(factorial(86))

# sqr = square(9)

# print(sqr)
# greet_user()
# aoa("saqib")



# Assignment 10 Function define karne hain def and lambda and use all the data structure 