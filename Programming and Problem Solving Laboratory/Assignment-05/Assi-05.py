# Problem Statement:
# To check whether input number is Armstrong number or not. An Armstrong number is an
# integer with three digits such that the sum of the cubes of its digits is equal to the number
# itself. Ex. 371.

number = int(input('Enter a number: '))

num_copy = number

sum_of_cubes = 0

while num_copy > 0:
    rem = num_copy % 10
    rem_cube = rem * rem * rem
    sum_of_cubes += rem_cube
    num_copy = int(num_copy / 10)

if sum_of_cubes == number:
    print(number, 'is an Armstrong No.')
else:
    print(number, 'is not an Armstrong No.')