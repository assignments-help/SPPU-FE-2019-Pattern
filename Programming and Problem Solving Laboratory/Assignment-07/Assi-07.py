# Problem Statement:
# To accept the number and Compute a) square root of number, b) Square of number, c)
# Cube of number d) check for prime, d) factorial of number e) prime factors

import math

def squre_root(num):
    return math.sqrt(num)

def square(num):
    return num * num

def cube(num):
    return num * num * num

def prime_no(num):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    
    return is_prime


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

def prime_factors(num):
    while num % 2 == 0:
        print(2)
        num = num / 2
         
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i== 0:
            print(i)
            num = num / i
             
    if num > 2:
        print(num)

print('Enter Choice')
print('0: Exit')
print('1: Square Root')
print('2: Square')
print('3: Cube')
print('4: Prime No.')
print('5: Factorial')
print('6: Prime Factors')

while True:
    choice = input('Enter Choice: ')

    if choice in ('0', '1', '2', '3', '4', '5', '6'):
        num = int(input('Enter the number: '))

        if choice == '0':
            break
        elif choice == '1':
            print('Square Root: ', squre_root(num))

        elif choice == '2':
            print('Square', square(num))

        elif choice == '3':
            print('Cube: ', cube(num))

        elif choice == '4':
            print('Prime No.: ', prime_no(num))

        elif choice == '5':
            print('Factorial: ', factorial(num))

        elif choice == '6':
            print('Prime Factors:')
            prime_factors(num)
    else:
        print('Invalid Input')

    
