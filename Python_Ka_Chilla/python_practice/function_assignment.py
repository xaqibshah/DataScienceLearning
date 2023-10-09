

# Function 01
def calculator(num1, num2):
    # num1 = input('Enter the first number')
    # num2 = input('Enter the second number')

    operator = input('Enter the operator: ')
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return 'Invalid operator'
    

print(calculator(5, 6))



# 02 function 

