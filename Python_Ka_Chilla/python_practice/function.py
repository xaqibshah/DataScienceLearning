# A function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function.
# function can return data as a result
# in python a function is defined using the def keyword

def greet_user():
    print('Hello user')


# greet_user()


def aoa():
    print('Asalam o alikum, All the way from Karachi')

# aoa()


def greet_user(username):
    print(f'Asalam o Alaekum, {username} !')



# greet_user('Saqib')

def aoa(name = 'khuda k bandy'):                    #for default value
    print(f'Asalam o Alaekum, {name} !')


# aoa('Ahmed')



def square(number ):
    return number * number 
 


# square(5)

# print(square(3))

# Recursion Function

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)



# print(factorial(4))


def recursive_print(number):
    if number == 0:
        return print(f'you just enter {number} that why run one time')              
    else:
        print(number)
        recursive_print(number-1)
    

recursive_print(6)



# lambda function

x = lambda a: a+10

print(x(5))


y = lambda a, b : a+b
#both are same
def y (a,b):
    return a+b


print(y(5, 6))

 


