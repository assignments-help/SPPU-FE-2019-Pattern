# Problem Statement:
# To simulate simple calculator that performs basic tasks such as addition, subtraction,
# multiplication and division with special operations like computing xy and x!.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def factorial(x):
    if x < 0:
        return -1
    elif x == 0:
        return 1
    else:
        fact = 1
        for i in range(1, x + 1):
            fact = fact * i
        return fact


print('Enter Choice')
print('1: Add')
print('2: Subtract')
print('3: Multiply')
print('4: Divide')
print('5: Power')
print('6: Factorial')

while True:
    choice = input('Enter Choice: ')

    if choice in ('0', '1', '2', '3', '4', '5', '6'):
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))

        if choice == '0':
            break
        elif choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))

        elif choice == '2':
            print(num1, '-', num2, '=', subtract(num1, num2))

        elif choice == '3':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
        elif choice == '5':
            print(num1, '^', num2, '=', power(num1, num2))
        elif choice == '6':
            print(num1, '!', '=', factorial(num1))
    else:
        print('Invalid Input')