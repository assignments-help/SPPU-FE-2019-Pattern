# Problem Statement:
# To accept N numbers from user. Compute and display maximum in list, minimum in list,
# sum and average of numbers.

n = int(input('Enter n: '))

arr = []

for i in range(n):
    x = int(input())
    arr.append(x)

min_num = arr[0]
max_num = arr[0]

for i in range(1, n):
    if max_num < arr[i]:
        max_num = arr[i]
    
    if min_num > arr[i]:
        min_num = arr[i]


print('Minimum No:', min_num)
print('Maximum No:', max_num)